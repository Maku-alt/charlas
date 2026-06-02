# Bibliografia

## Fuentes principales

- pandas installation docs: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
- pandas 2.3.0 release notes: https://pandas.pydata.org/pandas-docs/version/2.3/whatsnew/v2.3.0.html
- pandas 3.0.0 release notes: https://pandas.pydata.org/pandas-docs/stable/whatsnew/v3.0.0.html
- scikit-learn 1.7 release highlights: https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html
- scikit-learn 1.9 release highlights: https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_9_0.html
- SciPy 1.15.0 release notes: https://docs.scipy.org/doc/scipy-1.15.1/release/1.15.0-notes.html
- SciPy 1.17.0 release notes: https://docs.scipy.org/doc/scipy/release/1.17.0-notes.html
- Feature-engine 1.8 notes: https://feature-engine.trainindata.com/en/latest/whats_new/v_180.html
- Feature-engine 1.9 notes: https://feature-engine.trainindata.com/en/latest/whats_new/v_190.html
- OptBinning releases: https://github.com/guillermo-navas-palencia/optbinning/releases
- XGBoost 3.0 changes: https://xgboost.readthedocs.io/en/stable/changes/v3.0.0.html
- LightGBM releases: https://github.com/lightgbm-org/LightGBM/releases
- scikit-llm PyPI: https://pypi.org/project/scikit-llm/
- PandasAI PyPI: https://pypi.org/project/pandasai/
- Optuna PyPI: https://pypi.org/project/optuna/
- Optuna ask-and-tell tutorial: https://optuna.readthedocs.io/en/v3.4.1/tutorial/20_recipes/009_ask_and_tell.html
- DSPy optimizers docs: https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/optimization/optimizers.md
- Automatic Prompt Optimization with "Gradient Descent" and Beam Search: https://arxiv.org/abs/2305.03495
- PEP 20, The Zen of Python: https://peps.python.org/pep-0020/

## Fuentes contextuales usadas para la charla

- `compatibility-recommendation.md`
  - fuente principal para compatibilidad validada, tradeoffs y stacks recomendados
  - incluye links oficiales de releases, documentacion y paquetes

- `stack-baseline.md`
  - define el stack actual reportado por el usuario
  - fija el framing de la charla y las familias de librerias a revisar

- `library-gains-table.md`
  - sintetiza ganancia y tradeoff por libreria
  - aterriza el mensaje tecnico para audiencia de Data Science

## Nota de uso

- La charla combina fuentes oficiales de documentacion, release notes y metadatos de paquetes.
- Las recomendaciones de version se apoyan tanto en documentacion como en validacion practica local de instalaciones e imports.
- Las referencias a `Optuna`, `scikit-llm`, `PandasAI` y `DSPy` deben leerse como extensiones o capas opcionales sobre el stack base, no como reemplazo del stack clasico.
