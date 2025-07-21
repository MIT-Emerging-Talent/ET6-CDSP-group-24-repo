# Data Exploration

## TF-IDF Top Keywords by Theme

### [`top_keywords_per_theme.ipynb`](top_keywords_per_theme.ipynb)

### Purpose

This notebook analyzes categorized text data using TF-IDF (Term
Frequency-Inverse Document Frequency) to extract the top keywords per theme.
It's a structured alternative to topic modeling, relying on pre-assigned
themes.

### Datasets used

* `cleaned_datasets.csv`

### What It Does

* Applies TF-IDF vectorization to compute term importance within each theme.
* Extracts top keywords for each theme (based on TF-IDF score).
* Visualizes the top keywords per theme using bar plots.

### Outputs

* Keyword Ranking Tables: Top keywords per theme with TF-IDF scores.
* Bar Charts: Visual representations of top terms by theme.
* CSV File: Top keywords file for further use in Keywords in context (KWIC) analysis.

---
