import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(r"C:\Users\Victor\Proyectos\2026\charlas")
OUT = ROOT / "analysis" / "codex-token-audit"
PREV = Path(r"C:\Users\Victor\Documents\Codex\2026-06-29\importante-esta-tarea-es-para-diagnosticar\outputs\codex-usage-audit")
SESSION_DIR = Path(r"C:\Users\Victor\.codex\sessions\2026\06\28")

SESSION_FILES = [
    "rollout-2026-06-28T03-56-18-019f0d71-8d49-7fe2-82f1-f794eefbb000.jsonl",
    "rollout-2026-06-28T04-20-31-019f0d87-bb4f-71d3-84d8-f6903ec273b8.jsonl",
    "rollout-2026-06-28T04-56-40-019f0da8-d342-7ee2-b3c9-8e8394927c83.jsonl",
    "rollout-2026-06-28T04-57-31-019f0da9-9b46-7601-9c9c-8e01f1b0de23.jsonl",
    "rollout-2026-06-28T14-19-34-019f0fac-2c1d-74a0-ad8d-7323e42c5980.jsonl",
    "rollout-2026-06-28T14-24-17-019f0fb0-7d2e-7250-916a-54f7a1b39eea.jsonl",
    "rollout-2026-06-28T14-28-51-019f0fb4-a9c9-7193-b20d-e841958bb856.jsonl",
    "rollout-2026-06-28T14-31-36-019f0fb7-31d0-7613-a06a-3cdcc6b31888.jsonl",
    "rollout-2026-06-28T14-34-39-019f0fb9-f9f4-7f62-a952-d390733ca346.jsonl",
    "rollout-2026-06-28T14-37-06-019f0fbc-37dd-7110-8b75-838c6381a0e0.jsonl",
    "rollout-2026-06-28T14-45-07-019f0fc3-8e67-7881-9ccd-256c5e88127c.jsonl",
    "rollout-2026-06-28T15-39-29-019f0ff5-4704-7c31-aaa7-6e390f386e22.jsonl",
    "rollout-2026-06-28T21-54-48-019f114c-f32e-7c23-866e-7ace2f06ccd8.jsonl",
    "rollout-2026-06-28T21-58-37-019f1150-7292-7d62-bcbf-3eae9be578cf.jsonl",
    "rollout-2026-06-28T22-02-07-019f1153-a784-7fd3-9142-cfecf581597b.jsonl",
    "rollout-2026-06-28T22-14-17-019f115e-ca21-7d23-a956-1ef2e498c622.jsonl",
    "rollout-2026-06-28T22-19-12-019f1163-4821-7a30-92ae-5df9014c98d6.jsonl",
    "rollout-2026-06-28T22-50-56-019f1180-5896-71a1-bf1f-7672ce088270.jsonl",
    "rollout-2026-06-28T23-48-09-019f11b4-b788-7523-ac81-32655cdb3089.jsonl",
]

KEYWORDS = {
    "orchestrator": re.compile(r"orchestrator|orquestador", re.I),
    "spawn_agent": re.compile(r"spawn_agent", re.I),
    "wait_agent": re.compile(r"wait_agent", re.I),
    "close_agent": re.compile(r"close_agent", re.I),
    "view_image": re.compile(r"view_image", re.I),
    "handoff": re.compile(r"handoff|entrega|resumen compacto|compacto", re.I),
    "agent_log": re.compile(r"agent-log|logs?", re.I),
    "renders": re.compile(r"render|contact-sheet|Diapositiva|slide-\d+\.png", re.I),
    "knowledge_repo_01": re.compile(r"Knowledge Repo 01|Documentar Tablas", re.I),
    "full_specs": re.compile(r"templates[\\/]+charlas-sdd[\\/]+full|full[\\/]+.*spec", re.I),
}


def textish(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    try:
        return json.dumps(value, ensure_ascii=False)
    except TypeError:
        return str(value)


def usage_from_payload(payload):
    text = textish(payload)
    matches = re.findall(
        r'"(?:total_tokens|input_tokens|cached_input_tokens|output_tokens)"\s*:\s*\d+',
        text,
    )
    # Prefer direct JSON traversal because event shapes vary.
    found = []

    def walk(obj):
        if isinstance(obj, dict):
            keys = set(obj)
            if {"total_tokens", "input_tokens"}.intersection(keys):
                found.append(obj)
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)

    walk(payload)
    return found, matches


def get_usage_numbers(usage_obj):
    if not isinstance(usage_obj, dict):
        return {}
    details = usage_obj.get("input_token_details") or {}
    return {
        "total_tokens": int(usage_obj.get("total_tokens") or 0),
        "input_tokens": int(usage_obj.get("input_tokens") or 0),
        "cached_input_tokens": int(details.get("cached_tokens") or usage_obj.get("cached_input_tokens") or 0),
        "output_tokens": int(usage_obj.get("output_tokens") or 0),
    }


def infer_tool(item):
    if not isinstance(item, dict):
        return ""
    for key in ("name", "tool_name", "recipient_name"):
        if item.get(key):
            return str(item[key])
    if item.get("type") in {"function_call", "function_call_output"}:
        return str(item.get("call_id") or "")
    return ""


def scan_session(path):
    rows = []
    calls = []
    snippets = []
    events = Counter()
    keywords = Counter()
    usage_rows = []
    last_usage = None
    line_count = 0
    max_line_chars = 0
    session_id = ""
    first_ts = ""
    last_ts = ""
    meta_chars = 0
    turn_context_chars = []
    response_item_chars = []
    tools = Counter()
    function_output_chars = Counter()

    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            line_count = line_number
            max_line_chars = max(max_line_chars, len(line))
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = obj.get("timestamp") or ""
            first_ts = first_ts or ts
            last_ts = ts or last_ts
            typ = obj.get("type") or ""
            events[typ] += 1
            payload = obj.get("payload")
            payload_text = textish(payload)
            if typ == "session_meta":
                meta = payload if isinstance(payload, dict) else {}
                session_id = meta.get("session_id") or meta.get("id") or session_id
                meta_chars += len(payload_text)
            if typ == "turn_context":
                turn_context_chars.append(len(payload_text))
            if typ == "response_item":
                response_item_chars.append(len(payload_text))
                item = payload if isinstance(payload, dict) else {}
                tool = infer_tool(item)
                if tool:
                    tools[tool] += 1
                if item.get("type") == "function_call_output":
                    tools["function_call_output"] += 1
                    output = textish(item.get("output"))
                    function_output_chars[item.get("call_id") or "unknown"] += len(output)
            for name, pattern in KEYWORDS.items():
                if pattern.search(payload_text):
                    keywords[name] += 1
                    if len(snippets) < 80:
                        clean = re.sub(r"\s+", " ", payload_text)
                        snippets.append(
                            {
                                "file": path.name,
                                "line": line_number,
                                "timestamp": ts,
                                "type": typ,
                                "keyword": name,
                                "chars": len(payload_text),
                                "sample": clean[:500],
                            }
                        )
            usage_objs, _ = usage_from_payload(payload)
            for usage_obj in usage_objs:
                nums = get_usage_numbers(usage_obj)
                if nums.get("total_tokens"):
                    delta_total = ""
                    delta_cached = ""
                    delta_uncached = ""
                    if last_usage:
                        delta_total = nums["total_tokens"] - last_usage["total_tokens"]
                        delta_cached = nums["cached_input_tokens"] - last_usage["cached_input_tokens"]
                        uncached = nums["input_tokens"] - nums["cached_input_tokens"]
                        last_uncached = last_usage["input_tokens"] - last_usage["cached_input_tokens"]
                        delta_uncached = uncached - last_uncached
                    usage_rows.append(
                        {
                            "file": path.name,
                            "timestamp": ts,
                            "line": line_number,
                            "event_type": typ,
                            **nums,
                            "uncached_input_tokens": nums["input_tokens"] - nums["cached_input_tokens"],
                            "delta_total_tokens": delta_total,
                            "delta_cached_input_tokens": delta_cached,
                            "delta_uncached_input_tokens": delta_uncached,
                        }
                    )
                    last_usage = nums

    rows.append(
        {
            "file": path.name,
            "session_id": session_id,
            "first_timestamp": first_ts,
            "last_timestamp": last_ts,
            "line_count": line_count,
            "max_line_chars": max_line_chars,
            "session_meta_chars": meta_chars,
            "turn_context_count": len(turn_context_chars),
            "turn_context_chars_total": sum(turn_context_chars),
            "response_item_count": len(response_item_chars),
            "response_item_chars_total": sum(response_item_chars),
            "function_output_chars_total": sum(function_output_chars.values()),
            "top_events": "; ".join(f"{k}:{v}" for k, v in events.most_common(8)),
            "tools": "; ".join(f"{k}:{v}" for k, v in tools.most_common(15)),
            "keywords": "; ".join(f"{k}:{v}" for k, v in keywords.most_common()),
        }
    )
    return rows, usage_rows, calls, snippets


def write_csv(path, rows):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    summaries = []
    checkpoints = []
    snippets = []
    for name in SESSION_FILES:
        rows, usage_rows, _, snips = scan_session(SESSION_DIR / name)
        summaries.extend(rows)
        checkpoints.extend(usage_rows)
        snippets.extend(snips)

    write_csv(OUT / "session_event_summary.csv", summaries)
    write_csv(OUT / "usage_checkpoints_extracted.csv", checkpoints)
    write_csv(OUT / "keyword_snippets.csv", snippets)

    top_jumps = sorted(
        [r for r in checkpoints if isinstance(r.get("delta_total_tokens"), int)],
        key=lambda r: r["delta_total_tokens"],
        reverse=True,
    )[:80]
    write_csv(OUT / "top_token_jumps.csv", top_jumps)

    by_file = defaultdict(list)
    for r in checkpoints:
        by_file[r["file"]].append(r)
    compact = []
    for file, rows in by_file.items():
        rows = sorted(rows, key=lambda r: r["line"])
        if not rows:
            continue
        final = rows[-1]
        compact.append(
            {
                "file": file,
                "checkpoints": len(rows),
                "final_total_tokens": final["total_tokens"],
                "final_input_tokens": final["input_tokens"],
                "final_cached_input_tokens": final["cached_input_tokens"],
                "final_uncached_input_tokens": final["uncached_input_tokens"],
                "final_output_tokens": final["output_tokens"],
                "max_delta_total_tokens": max(
                    [r["delta_total_tokens"] for r in rows if isinstance(r.get("delta_total_tokens"), int)] or [0]
                ),
            }
        )
    write_csv(OUT / "usage_by_session_extracted.csv", sorted(compact, key=lambda r: r["final_total_tokens"], reverse=True))

    (OUT / "audit_manifest.json").write_text(
        json.dumps(
            {
                "sessions_scanned": len(SESSION_FILES),
                "outputs": [
                    "session_event_summary.csv",
                    "usage_checkpoints_extracted.csv",
                    "usage_by_session_extracted.csv",
                    "top_token_jumps.csv",
                    "keyword_snippets.csv",
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
