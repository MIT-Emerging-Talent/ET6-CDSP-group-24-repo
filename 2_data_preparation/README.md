# Data Preparation

## `cleaning_and_formatting_datasets.ipynb`

This notebook processes raw textual data extracted from PDF files located in the
datasets folder. It performs the following steps:

- **Extracts text** from PDF documents using `PyMuPDF` on a page-by-page basis.
- **Cleans and preprocesses the text** using `spaCy`, including removal of
stopwords, punctuation, and non-relevant tokens.
- **Stores the cleaned data** in a structured format by attaching the cleaned
text to each entry in a list of dictionaries.
- **Converts the data** into a pandas DataFrame for easy handling.
- **Exports the final output** as a CSV file named `cleaned_datasets.csv` into
the `/1_datasets` directory.

### 📥 Input

- Raw PDF files containing theme-specific text data to be processed.

### 📤 Output

- `/1_datasets/cleaned_datasets.csv` – Cleaned and structured text ready for
downstream NLP tasks such as keyword extraction or topic modeling.
