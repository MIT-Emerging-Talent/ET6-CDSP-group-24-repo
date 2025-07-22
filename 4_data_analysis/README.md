<!-- markdownlint-disable MD024 MD013 -->
# Data Analysis

We employed a hybrid analytical process: NLP Driven Analysis & Thematic Manual Coding.

## Topic Modeling with BERTopic

### [`Topic_Modeling_BERTopic.ipynb`](Topic_Modeling_BERTopic.ipynb)

This notebook applies **BERTopic**, a transformer-based topic modeling approach,
to analyze a text dataset focused on themes. The analysis helps uncover
**hidden themes or patterns** in the text and visualize them interactively.

### Datasets used

* `cleaned_datasets.csv`

### Key Features

* Loads pre-cleaned text data and filters by predefined thematic categories.
* Defines domain-specific stopwords to reduce noise and enhance topic clarity.
* Uses **UMAP** for dimensionality reduction and **HDBSCAN** for clustering.
* Applies BERTopic to generate interpretable topics.
* Visualizes topics through bar charts and interactive plots.

### Goals

* Identify key discussion patterns and shared language across themes.
* Explore how different topics cut across thematic boundaries.
* Support exploratory qualitative and thematic research.

---

## Keywords-in-Context (KWIC) Analysis by Theme

### [`keywords_in_context_analysis.ipynb`](keywords_in_context_analysis.ipynb)

This notebook performs a **Keywords-in-Context (KWIC)** analysis on a collection
of PDF documents organized by thematic categories. Using a set of pre-extracted
top keywords for each theme, the notebook extracts the surrounding context in
which each keyword appears within the documents.

### Datasets used

* All raw PDF files
* `per_theme_top_keywords.csv`

### Key Features

* Loads and extracts raw text from PDFs grouped by theme.
* Cleans and preprocesses text to ensure clean tokenization.
* Uses spaCy to tokenize text and identify keyword matches.
* Extracts and displays left and right context windows around each keyword.
* Provides structured, theme-specific outputs to support qualitative analysis.

### Goals

* Understand how key terms are framed within their thematic contexts.
* Support qualitative interpretation of textual data.
* Enable exploratory and descriptive insights across themes

This analysis is useful for exploring how critical terms are framed across
different topics.

## Manual Coding Process

Our manual analysis followed a structured qualitative coding workflow to extract insights from 7 documents, about 20% of our data pool. The goal was to identify exclusion patterns, thematic prevalence, and co-occurrence relationships between access-related issues.

We developed a shared codebook, manually coded excerpts using top-level themes and subcodes, and cleaned the data for analysis. Pivot tables were used to calculate theme frequency and co-occurrence patterns. We then wrote memos to interpret key themes and relationships.

See [`manual_analysis_technical_description.md`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-24-repo/tree/main/4_data_analysis) for a full explanation of our coding process and rationale.

---

## 🗂 Related Files

  [Coding Sheet (Google Sheet)](https://docs.google.com/spreadsheets/d/1ttROjrY1YECIfhm5oz4luWHxWq_MTShfQBsiFP1Pnvg/edit?gid=894372809#gid=894372809)
