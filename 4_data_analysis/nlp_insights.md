# NLP Thematic Insights

## 1. Introduction

This section presents an interpretation of the results from our topic modeling
analysis using BERTopic, applied to 38 documents grouped by thematic
categories. Rather than focusing on the methodology, which is
covered in the [Data Analysis Readme](/4_data_analysis/README.md),
the goal here is to understand what the generated topics and associated outputs
reveal about the underlying themes in the data.

We analyze and interpret several key outputs:

- **Topic word-score bar charts** – to evaluate keyword importance per topic.
- **Hierarchical clustering dendrogram** – to explore how topics group based on similarity.
- **Topic similarity matrix (heatmap)** – to highlight overlap and divergence among
topics.
- **2D topic space projection (UMAP)** – to visualize topic distribution and separability.
- **Theme-level keyword analysis** – to validate BERTopic findings and add
interpretive depth across predefined thematic categories.

These outputs are examined in the context of our research question, supported by
keyword-in-context (KWIC) examples and a thematic-level keyword breakdown, to
uncover deeper patterns in how organizations approach digital transformation in
training programs.

## 2. Topic Word-Score Bar Chart

![Topic Word Scores Bar Chart](/4_data_analysis/visuals/topic_word_scores.jpg)

The chart above displays the top keywords associated with each of the extracted
topics, highlighting what each topic is primarily "about." This allows us to
interpret how the discovered topics align with our qualitative findings derived
from manual coding.

### Topic–Finding Alignment

Each topic shows strong resonance with at least one of our
[six mixed-method findings](/4_data_analysis/mixed_methods_findings.md). Below
is a summary of how the topic model reflects and reinforces these broader themes:

- **Topic 1** aligns with **“Digital Divide Persists as a Foundational Barrier”**
capturing connectivity gaps, infrastructure deficits, and digital exclusion
across rural and socioeconomically marginalized populations.

- **Topic 4** and **Topic 6** reinforce both **“Inclusive Design Remains
Exceptional Despite Demonstrated Potential”** and
**“Policy Exists, But Implementation Is Weak”** highlighting assistive tech
potential, telecom failures, and systemic design gaps.

- **Topic 7** intersects with **“Social Exclusion Reinforces Systemic Barriers”**
particularly in how stigma, geography, and socioeconomic status compound
accessibility challenges.

- **Topic 0** reflects **“Inclusive Design Remains Exceptional”** showcasing
stories of innovation alongside continued marginalization due to inaccessible
tech and "afterthought" design.

- **Topic 9** relates to both **“Inclusive Design”** and
**“Informal Networks Bridge Gaps”** with mentions of usability testing and
financial access, suggesting local workarounds or grassroots tech use.

- **Topic 2** and **Topic 10** highlight themes in
**“Informal Networks Bridge Gaps”** and **“Policy/Partnerships”** through
entrepreneurship, social enterprise, and informal ecosystems supporting PWDs.

- **Topic 5** aligns with **“Policy Exists, But Implementation Is Weak”** and
**“Informal Networks”** emphasizing organizational efforts
(e.g., Safaricom, MTN, Sightsavers) that show promise but operate in silos.

This mapping supports the idea that unsupervised topic modeling
can meaningfully surface real-world barriers and enablers also observed through
qualitative analysis, providing mutual validation across methods.

## 3. Hierarchical Clustering

![Hierarchical Clustering](/4_data_analysis/visuals/hierarchical_clustering.jpg)

To explore how topics relate to one another, we applied hierarchical clustering
produced by BERTopic. The resulting dendrogram visualizes topic proximity in
terms of semantic meaning.

Key findings from the dendrogram include:

- **Cluster A: Digital Inclusion & Infrastructure**  
  Topics such as `0_centre_tech_accesstech`, `1_digital inclusion_internet`,
  and `4_funding_business_disability` are grouped closely. This suggests a
  shared thematic focus on the availability of technology infrastructure and
  funding opportunities that influence access and digital participation for
  disabled individuals.

- **Cluster B: AI and Innovation Ecosystem**  
  The dendrogram groups together `2_ai_young_entrepreneur`,
  `8_ai_dataset_governance`, and `5_incubator_programme_empowerment`, indicating
  a cohesive narrative around AI use, data governance, and programs fostering
  innovation and empowerment in marginalized communities.

- **Cluster C: Accessibility Tools and Workarounds**  
  Topics like `6_bypass_barriers_self-employed` and
  `3_jaws_screenreader_navigation` are semantically close, highlighting
  discussions around how disabled self-employed individuals use assistive
  technologies and creative workarounds to overcome systemic digital barriers.

- **Outlier Topic: Structural Legal Barriers**  
  Topic `7_legislation_regulation_exclusion` stands as an outlier, positioned
  further from other clusters. This indicates that conversations related to
  legal and regulatory exclusion are conceptually distinct and less frequently
  co-mentioned with the more practical or technological themes.

This clustering reveals that certain digital inclusion issues, such as access to
infrastructure, entrepreneurial support, and assistive technologies, tend to
co-occur, forming thematic cores. Meanwhile, legal exclusion appears to be a
unique area requiring separate analytical attention. These insights help us
prioritize how interventions might be bundled or tailored across policy and
programmatic responses.

## 4. Similarity Matrix

![Similarity Matrix](/4_data_analysis/visuals/similarity_matrix.jpg)

To further analyze topic relationships, a similarity matrix was generated using
BERTopic, based on cosine similarity between topic embeddings. The matrix
visually represents the semantic proximity among the 11 extracted topics. As
shown in the figure below, darker shades indicate higher similarity scores,
while lighter shades signify weaker associations.

The matrix reveals several insightful patterns:

- Topics `0_centre_tech_accesstech` and `6_telecom_director_outlet` show a
relatively high degree of similarity, suggesting a shared thematic focus around
technology access and infrastructure.
- Likewise, topic `1_digital inclusion_internet` aligns closely with
`8_ai_dataset_governance`, indicating overlapping concerns between digital
inclusion initiatives and governance of AI datasets.
- Conversely, topics such as `2_ai_young_entrepreneur` and
`5_inclusive datum_sightsavers` exhibit weaker similarity scores with other
topics, suggesting they address more distinct or specialized areas within the corpus.

The matrix provides a quantitative foundation to identify which themes may be
grouped together in broader clusters or require separate exploration in
subsequent analysis stages, such as hierarchical clustering or policy gap identification.

## 5. 2D Topic Space Visualization

![2D Topic Space](/4_data_analysis/visuals/2d_topic_space.jpg)

To further interpret the topic modeling results, we used BERTopic’s 2D
intertopic distance map, which provides a visual representation of the
relationships between the discovered topics in a reduced two-dimensional space.
This map was generated using UMAP (Uniform Manifold Approximation and
Projection) for dimensionality reduction.

### Key Observations

- **Topic Clustering**: Several topics form tight clusters, suggesting semantic
similarity and overlapping themes. For instance, a group of topics appears
concentrated near the center-right of the plot, indicating that they share
contextual relevance and may represent subthemes within a broader concept.

- **Topic Separation**: A few topics are more isolated from the cluster (e.g.,
Topic 0 on the far left), which indicates distinct semantic content. These
isolated topics may represent niche or highly specific themes that are different
from the core discussions in the dataset.

- **Topic Size**: The size of each circle reflects the frequency of the topic
across the corpus. Larger circles represent more dominant topics, while smaller
ones are less prevalent. This helps in identifying not only which topics are
common but also which may require closer investigation due to their specificity.

### Interpretation

The 2D topic space is useful for qualitative analysis of topic relationships.
By observing the spatial distances and groupings, we can understand how themes
in the dataset converge or diverge. Clusters may signal the need for combining
topics into a larger thematic category, whereas distant topics might merit
separate attention due to their uniqueness.

This visualization complements the dendrogram and topic representations by
offering a holistic view of semantic structure across the dataset.

## 6. Theme-Level Keyword Analysis

We organized our dataset by predefined themes. For each theme, we extracted the
top keywords to better understand the core semantic focus within each group of
documents. This analysis serves three purposes:

- **Validate BERTopic Topics**: Compare theme keywords with top keywords from topics.
- **Add Interpretive Depth**: Clarify what each theme emphasizes most, beyond
topic modeling.
- **Cross-Check Consistency**: Strengthen the overall reliability of findings.

### Theme 1: Barriers to Access

![Barriers to Access Keywords](/4_data_analysis/visuals/barriers_to_access_top_keywords.png)

**Top Keywords**: digital (0.48), access (0.34), mobile (0.30),
accessibility (0.28), technology (0.26), internet (0.25), service (0.23), ict (0.22)

**Semantic Focus**: This theme strongly emphasizes the fundamental
infrastructure and connectivity challenges. The dominance of "digital" (0.48)
and "access" (0.34) suggests that barriers are primarily conceptualized as
digital access issues rather than physical or social barriers alone. The
presence of "mobile" (0.30) and "internet" (0.25) indicates that mobile
connectivity and internet access are central concerns.

**BERTopic Validation**: This aligns with Topic 1 (digital inclusion/internet)
and Topic 6 (telecom/director/outlet), confirming that infrastructure and
connectivity barriers are consistently identified across different analytical approaches.

### Theme 2: Case Studies

![Case Studies Keywords](/4_data_analysis/visuals/case_studies_top_keywords.png)

**Top Keywords**: technology (0.30), source (0.30), riziki (0.29),
digital (0.28), education (0.25), inclusive (0.25), youth (0.23), support (0.22)

**Semantic Focus**: Case studies emphasize practical applications and success
stories, with "technology" and "source" tied for highest relevance (0.30). The
presence of "riziki" (0.29) suggests specific organizational or programmatic
examples. The focus on "education" (0.25) and "youth" (0.23) indicates that
case studies often feature educational interventions and youth-focused programs.

**BERTopic Validation**: This theme connects to Topic 2 (ai_young_entrepreneur)
and Topic 5 (incubator_programme_empowerment), showing that case studies
frequently document entrepreneurial and educational initiatives.

### Theme 3: Digital Infrastructure

![Digital Infrastructure Keywords](/4_data_analysis/visuals/digital_infrastructure_top_keywords.png)

**Top Keywords**: digital (0.54), access (0.41), inclusion (0.26), survey (0.23)
, service (0.22), internet (0.21), mobile (0.19), technology (0.18)

**Semantic Focus**: This theme has the strongest focus on "digital" (0.54)
among all themes, emphasizing the technical foundation of digital inclusion. The
high score for "access" (0.41) and "inclusion" (0.26) suggests that
infrastructure discussions are framed through an inclusion lens. The presence of
"survey" (0.23) indicates that infrastructure assessments often rely on
empirical data collection.

**BERTopic Validation**: Strongly validates Topic 1 (digital inclusion/internet)
and shows overlap with Topic 6 (telecom infrastructure), confirming that
infrastructure is a core concern across analytical methods.

### Theme 4: Inclusive Digital Technology

![Inclusive Digital Technology Keywords](/4_data_analysis/visuals/inclusive_digital_technology_top_keywords.png)

**Top Keywords**: digital (0.47), technology (0.43), accessibility (0.41),
access (0.27), ai (0.23), user (0.19), service (0.16), kenya (0.15)

**Semantic Focus**: This theme uniquely emphasizes "accessibility"
(0.41) alongside "technology" (0.43), suggesting a focus on technology design
and usability rather than just access. The presence of "ai" (0.23) indicates
that artificial intelligence is a significant component of inclusive technology
discussions. The mention of "kenya" (0.15) suggests geographic specificity in
some inclusive technology initiatives.

**BERTopic Validation**: Aligns with Topic 3 (jaws_screenreader_navigation)
and Topic 8 (ai_dataset_governance), confirming that assistive technologies and
AI governance are key components of inclusive digital technology discussions.

### Theme 5: Tech Ecosystem

![Tech Ecosystem Keywords](/4_data_analysis/visuals/tech_ecosystem_top_keywords.png)

**Top Keywords**: intellectual (0.42), employment (0.40), uganda (0.35), datum
(0.32), inclusive (0.30), work (0.18), national (0.17), inclusion (0.16)

**Semantic Focus**: This theme uniquely emphasizes "intellectual" (0.42) and
"employment" (0.40), suggesting a focus on intellectual disabilities and
employment opportunities. The focus on "datum" (0.32) suggests that data
collection and analysis are important for understanding tech ecosystem dynamics.

**BERTopic Validation**: Connects to Topic 5 (inclusive datum_sightsavers) and
shows some overlap with employment-related discussions, though the BERTopic
model may not have captured the specific focus on intellectual disabilities as prominently.

### Cross-Theme Patterns and Insights

**Access vs. Accessibility Distinction**: While "access" appears across multiple
themes, "accessibility" is most prominent in the inclusive_digital_technology
theme, suggesting a conceptual distinction between having access to technology
versus having technology that is accessible.

**Employment Focus**: The tech_ecosystem theme uniquely emphasizes
employment-related keywords, indicating that economic participation is a
distinct concern from technological access or design.

This theme-level analysis provides additional validation for our BERTopic
findings while revealing nuanced differences in how different aspects of digital
inclusion are conceptualized and discussed across our dataset.

## 7. Summary of Insights

Our NLP analysis reveals several key patterns that strengthen and
nuance our understanding of digital inclusion for persons with disabilities
in Sub-Saharan Africa. The convergence of BERTopic modeling and theme-level
keyword analysis provides robust validation while uncovering important
distinctions in how different aspects of the digital inclusion landscape are conceptualized.

### Core Patterns and Overlaps

**Infrastructure as Foundation**: Both BERTopic topics and theme keywords
consistently identify digital infrastructure and connectivity as central
concerns. Topic 1 (digital inclusion/internet) and the barriers_to_access theme
both emphasize "digital," "access," "mobile," and "internet" as dominant
keywords, confirming that basic connectivity remains the primary barrier to
digital inclusion.

**Technology Design vs. Access Distinction**: A clear conceptual separation
emerges between having access to technology versus having accessible technology.
The inclusive_digital_technology theme uniquely emphasizes "accessibility"
alongside "technology," while other themes focus more on "access" and "service."
This distinction is validated by Topic 3 (jaws_screenreader_navigation), which
specifically addresses assistive technologies.

### Other Interesting Findings and Contradictions

**Employment as Distinct Domain**: The tech_ecosystem theme uniquely
emphasizes employment-related keywords ("intellectual," "employment," "work"),
suggesting that economic participation represents a distinct concern from
technological access or design. This finding wasn't as prominently captured in
the BERTopic model, indicating that employment may be a specialized subdomain
requiring separate analytical attention.

**AI's Emerging Role**: Both Topic 8 (ai_dataset_governance) and the
inclusive_digital_technology theme highlight "ai" as a significant keyword,
suggesting that artificial intelligence is becoming a central component of
inclusive technology discussions. This represents an emerging trend that may
not have been as prominent in earlier digital inclusion literature.

**Data Collection Emphasis**: The digital_infrastructure theme's emphasis on
"survey" and the tech_ecosystem theme's focus on "datum" suggest that data
collection and analysis are becoming increasingly important for understanding
and addressing digital inclusion challenges.

### Methodological Validation

**Cross-Method Consistency**: The strong alignment between BERTopic topics
and theme-level keywords validates both analytical approaches. For instance,
Topic 1's focus on digital inclusion/internet directly corresponds to the high
"digital" and "access" scores in barriers_to_access and digital_infrastructure themes.

**Complementary Insights**: While BERTopic captured broader thematic clusters,
theme-level analysis revealed nuanced distinctions (e.g., the employment focus
in tech_ecosystem) that weren't as prominent in the topic model. This suggests
that combining unsupervised topic modeling with predefined thematic analysis
provides more comprehensive insights than either approach alone.

### Policy and Practice Implications

**Infrastructure Priority**: The consistent emphasis on connectivity and
infrastructure across all analytical methods suggests that basic digital access
remains the primary barrier, requiring continued investment in digital
infrastructure development.

**Design-Centered Approach**: The distinction between access and accessibility
suggests that policy interventions should address both connectivity gaps and
technology design simultaneously, rather than treating them as separate issues.

**Employment Integration**: The unique emphasis on employment in the
tech_ecosystem theme suggests that digital inclusion efforts should explicitly
integrate economic participation goals, particularly for persons with
intellectual disabilities.

This NLP analysis provides quantitative validation for qualitative findings
while revealing important nuances that can inform more targeted and effective
digital inclusion interventions. The convergence of multiple analytical
approaches strengthens confidence in these insights while highlighting areas
that may require specialized attention in future research and policy development.
