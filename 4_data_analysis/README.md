# Data Analysis

We combined **natural language processing (NLP)** and **manual qualitative
coding** to uncover patterns of exclusion from a text-based dataset.
This hybrid approach enabled us to scale insights, validate patterns across
methods, and balance exploratory techniques with close thematic reading.

---

## 💻 NLP-Driven Computational Analysis

Our computational workflow began with **data cleaning and preprocessing** using
Python libraries like [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) and
[spaCy](https://spacy.io/). This transformed raw PDFs into a clean, structured
corpus:  
📄 [`cleaned_datasets.csv`](../1_datasets/processed_data/cleaned_datasets.csv)

We applied several NLP techniques to analyze the data:

---

### 1. [Data Exploration](../3_data_exploration/README.md)

We began by validating our dataset for completeness, theme coverage, and text
quality—ensuring a solid foundation for downstream analysis.

---

### 2. [Keyword-in-Context (KWIC)](./keywords_in_context_analysis.ipynb)

This qualitative technique allowed us to pinpoint direct mentions and understand
 the nuanced context of key terms (e.g., **'digital'**, **'AI'**,
**'exclude'**,**'disability'**,
**'self-employed'**)
within the text. This provided granular, sentence-level evidence for our hypothesis.

**Why KWIC?**

* Understand how key terms are framed within their thematic contexts.
* Support qualitative interpretation of textual data.
* Enable exploratory and descriptive insights across themes.

This analysis is useful for exploring how critical terms are framed across
different topics.

---

### 3. [Term Frequency-Inverse Document Frequency (TF-IDF) Keyword Analysis](../3_data_exploration/top_keywords_per_theme.ipynb)

TF-IDF helped surface the most **statistically significant and distinctive**
words per theme. This provided a quantitative view of language patterns,
complementing our KWIC analysis and supporting cross-theme comparison.

---

### 4. [Topic Modeling with BERTopic](./Topic_Modeling.ipynb)

We used [**BERTopic**](https://maartengr.github.io/BERTopic/index.html) as an
advanced neural technique to discover **latent, naturally emerging conceptual
themes** within our dataset, moving beyond predefined categories. It achieves
this by generating document embeddings and clustering similar passages into
semantically rich topic groups.

**Key Features & Process:**

* Custom stopwords for noise reduction and enhanced clarity
* **UMAP** for dimensionality reduction and **HDBSCAN** for clustering
* Interactive visualizations showcasing topic relationships and hierarchy

---

### 📊 Visual Outputs

Explore key insights from our topic modeling through these visualizations:
<!-- markdownlint-disable MD033 MD013 MD041-->
|                                          |                                          |
| :--------------------------------------- | :--------------------------------------- |
| <div style="text-align: center;">           | <div style="text-align: center;">           |
|   ![Topic Word Scores Bar Chart](./visuals/topic_word_scores.jpg)<br> |   ![Hierarchical Clustering Dendrogram](./visuals/hierarchical_clustering.jpg)<br> |
|   <strong>Topic Word Scores</strong>: <span style="font-style: italic;">Shows most important words and their scores per topic.</span> |   <strong>Hierarchical Clustering</strong>: <span style="font-style: italic;">Reveals the hierarchical structure of topics and their relationships.</span> |
| </div>                                   | </div>                                   |
| <div style="text-align: center;">           | <div style="text-align: center;">           |
|   ![Similarity Matrix](./visuals/similarity_matrix.jpg)<br> |   ![2D Topic Space](./visuals/2d_topic_space.jpg)<br> |
|   <strong>Similarity Matrix</strong>: <span style="font-style: italic;">Illustrates topic similarity; darker colors indicate higher resemblance.</span> |   <strong>2D Topic Space</strong>: <span style="font-style: italic;">Plots topics as circles in 2D space where proximity indicates semantic relatedness.</span> |
| </div>                                   | </div>                                   |

---

## 📝 Manual Coding Process

In parallel, we conducted a **structured manual coding** of 7 documents (~20%
of our dataset), guided by a collaboratively developed codebook covering core
themes and subcodes.
See [Manual Coding Technical Write-up](./manual_analysis_technical_description.md)
for a full explanation of our coding process and rationale.  

**Our process involved:**

* Applying top-level theme codes, subcodes and shared tags to excerpts using
  our codebook.
* Utilizing pivot tables to examine theme frequency and co-occurrence.
* Writing coding memos to interpret both expected and surprising findings.
<!-- markdownlint-disable MD059-->
**Access our Manual Coding Sheet**
**[here](https://docs.google.com/spreadsheets/d/1ttROjrY1YECIfhm5oz4luWHxWq_MTShfQBsiFP1Pnvg/edit?gid=894372809#gid=894372809)**.
<!-- markdownlint-enable MD059-->
---

## 💡 Key Findings and Insights

Our mixed-methods analysis, combining computational patterns with in-depth qualitative interpretation, yielded critical insights into digital exclusion and its impacts.

> *For a more detailed breakdown of all findings and their evidence: [**Detailed Findings Document**](./mixed_methods_findings.md)*

1. **Access Barriers**: Connectivity and affordability dominated manual coding, while NLP revealed distinct topics for affordability, device access, and poor connectivity. Keyword extraction reinforced these as core exclusion drivers.

2. **Digital Skills Gaps**: Despite tool availability, gaps in skills and training—surfaced through hybrid analysis—create the illusion of inclusion without true usability.

3. **Design Fragmentation**: Manual coding showed that inclusive tools (e.g., JAWS, Be My Eyes) exist but remain isolated exceptions, not the norm in digital design.

4. **Policy–Practice Gap**: Hybrid findings highlighted a disconnect between strong legal frameworks (e.g., Rwanda) and weak implementation, with NLP linking policy language to reports of poor follow-through.

5. **Social & Systemic Exclusion**: Our hybrid analysis traced digital exclusion to deeper forces—stigma, invisibility, and top-down design—that marginalize PWDs in both data and decision-making.

6. **Peer Networks**: Manual coding found peer-led solutions to be the most consistent and effective form of resilience, often compensating for systemic neglect.

7. **Siloed Collaborations**: NLP surfaced patterns of collaboration that remain fragmented, limiting their reach and potential for systemic change.

---

[← Back to Project Overview](./../README.md)
