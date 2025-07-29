<!-- markdownlint-disable MD033 MD013 MD041-->
<div align="center">
  <img src="https://github.com/user-attachments/assets/5d6ef4b5-3104-474c-8a3e-05d7b84b75a0" alt="CrystalPearl Rising Logo" width="450"/>
</div>
<!-- markdownlint-enable MD033 MD013 MD041-->

<!-- markdownlint-disable MD013-->
<div align="center">

# Offline by Design  
<!-- markdownlint-disable MD001-->
### *How digital systems exclude by default*
<!-- markdownlint-enable MD001-->
</div>

---

### Crystal Pearl – Project Team  

*Disability. Design. Digital Inclusion.*

Like crystals formed under pressure and pearls revealed through care, people with disabilities hold strength, creativity, and resilience that's too often overlooked. This project investigates how digital technologies are shaping economic opportunities—and exclusions—for self-employed people with disabilities in Sub-Saharan (SSA).

---

## What This Repository Covers

This repo documents our full project journey, milestone by milestone. From defining a problem close to home, to collecting real-world data, to analyzing where digital tools help or hinder, we trace the full arc of a data science research project.

You’ll find:

* Our research question and background
* A structured dataset built from qualitative sources
* Analysis using both manual coding and NLP tools
* Insights into how exclusion happens—and what can be done
* Communication and collaboration materials

---

## Our Research Question

**How do digital technologies exclude self-employed individuals with disabilities in Sub-Saharan Africa (SSA)?**

We're asking this to understand not just the tech, but the human experience behind the interface: What works, what doesn't, and why?  This focused approach was carefully shaped by our project's defined research scope, the nature of available qualitative data, and the practical operational constraints detailed in our [Constraints](collaboration/constraints.md) document.

>*See our definition of self-employment within the [domain study](0_domain_study/README.md#defining-our-scope).*

---

## Research Conclusion

Digital exclusion for self-employed people with disabilities in Sub-Saharan Africa is shaped by overlapping structural, technological, and systemic barriers—from unaffordable services and inaccessible design to weak policy enforcement and pervasive stigma.

Our hybrid analysis shows that exclusion is not just about lack of access—it’s about how systems are built, who they are built for, and who gets left out. Resilience through local innovation and peer networks is real, but these efforts often arise from necessity—not choice—and should not substitute for systemic change.

We also found that disability-led innovation is both feasible and underutilized. There is a powerful opportunity here: to shift from workarounds to co-designed, inclusive systems that prioritize accessibility from the start.

---

## Milestones Overview
<!-- markdownlint-disable MD033 MD013-->
<details>
<summary><strong>Milestone 0: Cross-Cultural Collaboration – <em>Complete</em></strong></summary>

We kicked off the project by aligning how we work as a team:

* Defined group norms and communication plans
* Set clear constraints and goals
* Built our project board and repo structure

Key docs:

* [Group Norms](collaboration/README.md)
* [Constraints](collaboration/constraints.md)
* [Learning Goals](collaboration/learning_goals.md)
* [Retrospective](collaboration/retrospectives/0_cross_cultural_collaboration.md)

---

</details>

<details>
<summary><strong>Milestone 1: Problem Identification – <em>Complete</em></strong></summary>

In this milestone, we explored our problem domain through systems thinking and human-centered framing. We clarified what digital exclusion really means for self-employed people with disabilities in Sub-Saharan Africa.

Our research question:

> **How do digital technologies exclude self-employed people with disabilities in Sub-Saharan Africa (SSA)?**

This question emerged from a careful review of structural, design, and systemic barriers, and is grounded in both lived experience and policy blind spots.
<!-- markdownlint-disable MD059-->
* Dive into the [full problem framing and rationale](0_domain_study/problem_statement.md)
* See why this research matters, beyond just accessibility [here](0_domain_study/problem_statement.md#why-this-research-matters)
* Explore our [background domain review](0_domain_study/background_review.md)
* Track how our [initial research questions evolved](0_domain_study/research_notes/initial_research_questions.md)
* Understand the [Iceberg Model of Digital Exclusion](0_domain_study/background_review.md#63-iceberg-model-of-digital-exclusion)
  that complements our research question by revealing how much exclusion is structural,
  not just technical.
* Milestone 1 → ✓ [Retrospective](collaboration/retrospectives/1_problem_identification.md)

---

</details>

</details>

<details>
<summary><strong>Milestone 2: Data Collection – <em>Complete</em></strong></summary>

### Our Qualitative-First Approach to Understanding Digital Exclusion

To truly understand the **digital exclusion of self-employed people with disabilities in Sub-Saharan Africa**, we adopted a **qualitative-first approach**. Existing quantitative data in this space is limited—and often fails to capture the nuanced, lived realities of exclusion.

To address this, we centered our methodology on a qualitative data model, moving beyond simple numbers. We meticulously collected *38 narrative-rich documents*—ranging from NGO reports to policy briefs to media stories—and structured them into a custom dataset for both manual and automated analysis.

> 📌 This approach helped us uncover patterns of exclusion that are contextual, subtle, and often missing from traditional datasets.

**Our process involved:**

* Developing a **structured dataset** from real-world narratives  across five core themes
* Implementing robust **cleaning and extraction scripts** to transform raw PDFs into a unified, analyzable format.
* **Cleaning, labeling, and documenting all sources**, explaining **flaws, gaps, and decisions** transparently in our metadata.

<div align="center">
  <img src="https://github.com/user-attachments/assets/a62fcd5c-7543-4f23-a1de-6e680e89e9c8" alt="Qualitative Modeling Flowchart" width="600"/>
  <br><em>Visualizing our qualitative data modeling pipeline</em>
</div>

Key docs:

* [Explore Our Datasets](1_datasets/) — Access thematic folders, source documents, and processed data.
* [Understand Our Data Modeling Approach](1_datasets/modeling_approach.md) — Learn how and why we structured our qualitative data, including its rationale and limitations.
* [Recreate Our Processed Dataset](1_datasets/README.md#recreating-our-processed-dataset) — Follow steps to regenerate the cleaned and structured data from raw sources.
* [View Our Processed Data Directly](1_datasets/processed_data/) — Access the final, cleaned CSV files for immediate review.
* [See the Group Retrospective for Data Collection](collaboration/retrospectives/2_data_collection_group_retrospective.md) — Insights and learnings from our data collection process.

---

</details>

<details>
<summary><strong>Milestone 3: Data Analysis – <em>Complete</em></strong></summary>

### Mixed Methods Analysis Summary

To explore digital exclusion and its economic impacts on persons with
disabilities (PWDs), we used a **hybrid method** combining manual
qualitative coding with automated natural language processing (NLP). This let
us surface both **fine-grained patterns** and **emergent themes** across our dataset that might be overlooked in close reading alone.

### Methods at a Glance

* **Manual Coding**:

    We manually analyzed a subset of 7 documents (roughly 20% of our corpus), employing a **hybrid deductive–inductive thematic coding approach** with a collaboratively developed codebook centered on key themes: access, design, policy, and systemic exclusion. While direct data on PWD entrepreneurs was limited, **proxy indicators** (e.g., digital literacy gaps, telecom inaccessibility) allowed us to infer challenges relevant to self-employed individuals with disabilities. This rigorous process, including **intercoder calibration**, yielded rich thematic insights and co-occurrence patterns.

* **NLP-Assisted Analysis**:

    To complement the manual coding and expand our reach, we applied several NLP techniques:

  * [Keyword-in-Context (KWIC)](./4_data_analysis/keywords_in_context_analysis.ipynb) — to understand how key terms like *"AI"*, *"self-employed"*, or *"exclusion"* appear in narrative context
  * [TF-IDF Keyword Analysis](./3_data_exploration/top_keywords_per_theme.ipynb) — to extract statistically important keywords by theme
  * [BERTopic Modeling](./4_data_analysis/Topic_Modeling.ipynb) — to discover latent topic clusters and relationships using neural embeddings

These approaches let us move beyond pre-coded themes and uncover hidden signals across the full dataset.

---

### Key Findings

1. **Access Barriers**: Affordability dominated manual coding, while NLP revealed distinct topics for affordability, device access, and poor connectivity. Keyword extraction reinforced these as core exclusion drivers.

2. **Digital Skills Gaps**: Despite tool availability, gaps in skills and training—surfaced through hybrid analysis—create the illusion of inclusion without true usability.

3. **Design Fragmentation**: Manual coding showed that inclusive tools (e.g., JAWS, Be My Eyes) exist but remain isolated exceptions, not the norm in digital design.

4. **Policy–Practice Gap**: Hybrid findings highlighted a disconnect between strong legal frameworks (e.g., Rwanda) and weak implementation, with NLP linking policy language to reports of poor follow-through.

5. **Social & Systemic Exclusion**: Our hybrid analysis traced digital exclusion to deeper forces—stigma, invisibility, and top-down design—that marginalize PWDs in both data and decision-making.

6. **Peer Networks**: Manual coding found peer-led solutions to be the most consistent and effective form of resilience, often compensating for systemic neglect.

7. **Siloed Collaborations**: NLP surfaced patterns of collaboration that remain fragmented, limiting their reach and potential for systemic change.

---

### Confidence in Results

#### Manual Analysis Confidence

* **High confidence** in dominant patterns (e.g., affordability, literacy gaps),
    as they appeared across documents and coders.
* **Moderate confidence** in less frequent or inferred patterns due to
    subjectivity, sample size (7 docs), and reliance on proxy data.

#### NLP Confidence

* **Exploratory value only.** NLP helped affirm and expand our findings. But it is limited by:
  * Text quality and preprocessing
  * Interpretability of unsupervised topic clusters
  * Manual labeling of topics and keyword choices
  * Potential for overfitting or thematic overlap.

---

### Known Limitations

While our hybrid analysis offers both depth and breadth, several limitations should be acknowledged:

* **Small & Uneven Dataset**: Our analysis relied on only 38 documents of varying depth and format, potentially limiting the generalizability of our findings.
* **Reliance on Proxy Data**: Direct insights into PWD entrepreneurs' experiences were limited, requiring inferences from broader indicators of access and inclusion.
* **Manual Coding Subjectivity**: Despite a shared codebook and cross-validation, manual analysis inherently involves interpretive subjectivity from researchers.
* **NLP Context Limitations**: NLP models captured linguistic patterns but often underrepresented contextual nuance, cultural specificity, or implicit meaning from lived experiences.
* **Lack of Disaggregated Data**: Absence of demographic breakdowns (e.g., gender, age, rural-urban) in documents constrained our ability to draw intersectional insights.
* **Time Constraints**: Project timelines limited deeper narrative synthesis and external stakeholder validation of findings.

---

### 🔮 Ideas for Future Research

* Focused studies on underrepresented groups (e.g., women with disabilities)
* Longitudinal or case-based studies to examine how inclusion efforts evolve over time.
* Audits of algorithmic bias especially in platform-based or informal digital work.
* Training NLP models using this codebook to scale future thematic analysis across the full dataset.

---

Key docs:

* [See full technical explanation here](https://www.google.com/search?q=./4_data_analysis/manual_analysis_technical_description.md) — Detailed explanation of the manual qualitative coding methodology.
* [See Manual Analysis Insights](https://www.google.com/search?q=./4_data_analysis/manual_analysis_insights.md) — Key findings and insights derived from manual qualitative analysis.
* [See NLP Analysis Visuals](https://www.google.com/search?q=./4_data_analysis/README.md) — Visualizations and an overview of the NLP-assisted analysis results.
* [All notebooks/scripts](https://www.google.com/search?q=./4_data_analysis) — Access all analytical scripts and Jupyter notebooks used in the data analysis phase.
* [See the Group Retrospective for Data Analysis](collaboration/retrospectives/3_data_analysis_group_retrospective.md) — Insights and learnings from our data analysis process.
  
---

</details>

</details>

<details>
<summary><strong>Milestone 4: Communicating Results – <em>In Progress</em></strong></summary>

We're working on a communication strategy aimed at:

* Translating our insights into accessible, actionable messages
* Choosing the right format for impact
* Tailoring to our intended audience (e.g., policy, industry, disabled entrepreneurs)

Key docs (WIP):

* [Communication Plan](5_communication_strategy/4_communicating_results_group.md)

---

</details>

<details>
<summary><strong>Milestone 5: Final Presentation – <em>Pending</em></strong></summary>

Final showcase will include:

* A 1-minute project pitch
* A 3-minute walkthrough of our process and findings
* Slide deck or presentation artifact

Key docs (coming soon):

* [Final Presentation Materials](6_final_presentation/)

</details>

---

## Repository Structure

```text
├── README.md                    # This file
├── 0_domain_study/              # Domain research
│   ├── problem_statement.md     # Problem framing + final research question + rationale
│   ├── background_review.md     # Domain scan: inclusion gaps, tech actors, iceberg model
│   ├── guide.md                 # Navigation aid
│   └── research_notes/          # Early-stage thinking and team contributions
├── 1_datasets/                  # Data collection
│   ├── barriers_to_access/      # Raw documents related to access barriers
│   ├── case_studies/            # Raw documents containing case studies
│   ├── digital_infrastructure/  # Raw documents related to digital infrastructure
│   ├── inclusive_digital_technology/ # Raw documents on inclusive digital technology
│   ├── processed_data/          # Cleaned and structured data (CSV files)
│   ├── tech_ecosystem/          # Raw documents related to the tech ecosystem
│   ├── guide.md                 # Navigation aid for the datasets directory
│   ├── modeling_approach.md     # Explanation of the qualitative data modeling approach
│   └── README.md                # Overview of the data collection strategy
├── 2_data_preparation/          # Cleaning + structuring
│   ├── cleaning_and_formatting_datasets.ipynb # Jupyter notebook for data cleaning and formatting
│   ├── guide.md                 # Navigation aid for data preparation files
│   └── README.md                # Overview of the data preparation process
├── 3_data_exploration/          # Early NLP + keyword analysis
│   ├── guide.md                 # Navigation aid for data exploration files
│   ├── README.md                # Overview of the data exploration strategy
│   └── top_keywords_per_theme.ipynb # Jupyter notebook for TF-IDF keyword analysis
├── 4_data_analysis/             # Manual & NLP analysis results
│   ├── visuals/                 # Visualizations from NLP topic modeling & clustering
│   ├── guide.md                 # Navigation aid for the analysis directory
│   ├── keywords_in_context_analysis.ipynb # Jupyter notebook for KWIC analysis
│   ├── manual_analysis_insights.md    # Summary of insights from manual coding
│   ├── manual_analysis_technical_description.md # Detailed methodology for manual coding
│   ├── README.md                      # Overview of the data analysis strategy
│   └── Topic_Modeling.ipynb           # Jupyter notebook for BERTopic modeling
├── 5_communication_strategy/   # Messaging and impact plan (in progress)
├── 6_final_presentation/       # Final pitch and summary (pending)
├── collaboration/              # Norms, goals, retrospectives
├── notes/                      # Scratchpad + extra thinking
└── requirements.txt            # Dependencies

```

---

## Team

| Name                     | GitHub                                             |
| ------------------------ | -------------------------------------------------- |
| Jola-Moses               | [@jola-ds](https://github.com/jola-ds)             |
| Karim Makie              | [@KarimMakki](https://github.com/KarimMakki)       |
| Muqadsa Tahir            | [@MuqadsaT](https://github.com/MuqadsaT)           |
| Omer Dafaalla            | [@omerdafaalla](https://github.com/omerdafaalla)   |
| Omnia Mustafa Abdulgadir | [@Omnia-Agabani](https://github.com/Omnia-Agabani) |
| Robel Mengsteab          | [@robi-mengs](https://github.com/robi-mengs)       |

---

### How to Contribute

* Fork this repo and open a pull request
* See [CONTRIBUTING.md](CONTRIBUTING.md)
* Use issues or discussions to flag bugs, questions, or ideas

## License

[MIT License](LICENSE)

---

*Last updated: 29 July 2025*
