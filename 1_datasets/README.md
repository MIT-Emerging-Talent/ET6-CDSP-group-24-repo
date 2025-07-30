<!-- markdownlint-disable MD013 -->
# 📂 Dataset Directory

This folder documents the datasets used in our research on **digital exclusion of persons with disabilities (PWDs) in Sub-Saharan Africa (SSA)**, with a particular focus on self-employed individuals.

## Purpose

  This directory aims to ensure **transparency, reproducibility, and clarity** around our data sources. We worked with a variety of qualitative and unstructured sources, and our goal was to:

- Capture contextual insights not found in structured datasets.
- Support thematic analysis by organizing datasets around recurring domains (e.g., inclusive technology, digital infrastructure, case studies).
- Enable others to trace and understand how our evidence base connects to our central research question.
- For a detailed explanation of our qualitative data modeling approach and its rationale, *please see [Our Qualitative Data Modeling Approach](./modeling_approach.md).*

## Documentation Approach

Each dataset is documented using a structured format that includes:

- A brief **summary description**
- A **collapsible metadata section** with:
  - Source  
  - Type of dataset (e.g., report, article, survey)  
  - Timeframe  
  - File format (e.g., PDF)
  - Connection to research question
  - Noted limitations
- Direct **source link**

> ✅ Note: We refer to each item as a "dataset" even if it's an article, policy report, or survey, as all are treated as **evidence units** in qualitative analysis.

---

## 📁 Directory Guide

This folder is divided into sub-files based on **thematic categories**, each in its own `.md` file:

- [barriers_to_access](barriers_to_access/README.md) – Enablers of digital exclusion
- [case_studies](case_studies/README.md) - Lived experiences of disabled self employed individuals
- [digital_infrastructure](digital_infrastructure/README.md) – Access, connectivity, infrastructure gaps
- [inclusive_digital_technology](inclusive_digital_technology/README.md) – Accessibility features (or flaws), and AI-driven exclusion
- [tech-ecosystem](tech_ecosystem/README.md) - Actor accountability (design, funding, policy, feedback loops)
- [irrelevant_datasets](irrelevant_datasets.md) - are no longer in use, as it is not suitable for our upcoming NLP analysis phase
- `processed_data` - is a folder that contains processed datasets
  which are [`cleaned_datasets.csv`](../1_datasets/processed_data/cleaned_datasets.csv) and the [`per_theme_top_keywords.csv`](./processed_data/per_theme_top_keywords.csv)
Each theme folder contains list of pdfs with a README.md file that describes a summarized description of the datasets inside the theme.

---

## Criteria for Inclusion

We included datasets that:

- Focus on **Sub-Saharan Africa** (regional or country-level)
- Mention **persons with disabilities**, with a focus on **self employers**
- Relate to **digital technologies**, **mobile platforms**, or **AI**
- Offer insights into **barriers, usage patterns, or enablers**

Sources include government reports, NGO briefs, academic publications, media articles, and others.

---

## 🔁 Recreating Our Processed Dataset

This section shows how anyone can reproduce our cleaned and structured dataset directly from the raw PDF sources.

### Steps

1. **Download raw PDFs**
   Source documents are located in subfolders inside [`1_datasets`](../1_datasets), organized by theme (e.g., `barriers_to_access`, `case_studies`).

2. **Run our data preparation script**
   Navigate to [`2_data_preparation`](../2_data_preparation) and open
   [`cleaning_and_formatting_datasets.ipynb`](../2_data_preparation/cleaning_and_formatting_datasets.ipynb).
   This script:

   - Extracts and cleans text from PDFs
   - Structures entries into a unified table
   - Saves output as `cleaned_datasets.csv`

3. **Explore outputs**
   Final structured data and keyword tables are in:

   - [`cleaned_datasets.csv`](./processed_data/cleaned_datasets.csv)
   - [`per_theme_top_keywords.csv`](./processed_data/per_theme_top_keywords.csv)

> ⚠️ Requires Python 3.10+, `PyMuPDF`, `spaCy`, `pandas`, `matplotlib`, and `scikit-learn`.

---

## 📌 Additional Notes

- We included **both high-level reports** and **micro-level stories** to account for systemic patterns and individual experience.
- Some sources may lack granular disability data; limitations are always disclosed in the metadata.

[← Back to Project Overview](../README.md)
