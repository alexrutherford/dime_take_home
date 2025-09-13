# dime_take_home

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Take home test for DIME World Bank

## High Level Description

This repo uses the provided data files on

- Taxonomy of terms related to food security in Arabic and English
- Location information mapping variations of admin 0/1/2 names to unique ids
- Corpus of English and Arabic news articles from 1 month in 2024

## Approach

- Notebook [00_eda.ipynb](notebooks/00_eda.ipynb) Examines the datasets for missing values, sparsity and volumes. Translates missing Arabic terms in taxonomy using an LLM. Writes some convenience files e.g. revese mapping of locations and ids
- Notebook [01_processing.ipynb](notebooks/01_processing.ipynb) Extracts locations and risk factors from articles, drops those articles matchng neither.
- Notebook [02_analysis.ipynb](notebooks/02_analysis.ipynb) Looks at daily volumes of risk factors and admin 0/1/2 in both languages. Computes some simple correlations between these in each language.
- Notebook [03_validation.ipynb](notebooks/03_validation.ipynb)

## Future Work

There is much that could be improved with more time.

- Without knowing where the taxonomy terms came from, it is likely that it could be augmented using a snowball approach. i.e. look for new n-grams which coincide uniquely with n-grams in the taxonomy.
- Instead of using keyword matching, use an LLM to tag articles with risk factors in either (i) a zero shot fashion, possibly using official definitions of food insecurity terms or (ii) a few-shot learning approach with some examples of articles and their tags or (iii) a supervised-fine tuning approach in which the LLM is fine-tuned on articles and tags. Note that these would need to be evaluated.
- The most important task is validation of this approach using some ground truth data. This would nee to overlap in the time period and countries and ideally be at sub-national granularity. It is unlikely that the frequency would be more than monthly which is challenging with only 1 month of text corpus data.
- Much f the code is copy-pasted to repeat for Arabic and English. Ideally this would all be wrapped in a function with a language flag.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         dime_take_home and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── dime_take_home   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes dime_take_home a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

