# Federated Machine Learning: Concept and Applications

**Full citation:** Yang, Q., Liu, Y., Chen, T., Tong, Y. (2019). Federated Machine Learning: Concept and Applications. ACM Transactions on Intelligent Systems and Technology, 10(2), Article 12, 1-19. DOI: 10.1145/3298981. arXiv:1902.04885.

**PDF:** [arXiv](https://arxiv.org/abs/1902.04885)

**Verification note:** Bibliographic details confirmed via WebSearch (ACM DL, DBLP, ResearchGate). Abstract-level verified.

**Linked concepts:** [[Federated_Learning]]

## Abstract summary

The paper that established federated learning's modern conceptual framework, defining and distinguishing horizontal federated learning (shared feature space, different samples), vertical federated learning (shared samples, different feature spaces), and federated transfer learning, alongside a secure aggregation architecture preserving data privacy across participants.

## Research problem

Data silos and privacy regulation prevent organizations from pooling data for centralized model training, but no shared conceptual framework existed for classifying the different ways multiple parties could collaboratively train a model without sharing raw data.

## Key idea

Classify collaborative, privacy-preserving learning setups by how participants' data overlaps in the sample-versus-feature space (horizontal, vertical, or transfer), giving the field a shared vocabulary and taxonomy.

## Technical contribution

The horizontal/vertical/transfer federated learning taxonomy that essentially all subsequent federated learning literature (including every other paper in this KB's Federated_Learning concept) uses or assumes; a secure, privacy-preserving aggregation framework for each setting.

## Experimental methodology

Conceptual framework paper with illustrative applications (e.g., cross-organization risk modeling) rather than a single benchmark-driven empirical study.

## Results

Established the terminology and taxonomy (horizontal/vertical/transfer FL) that structures the entire federated learning field; became the most-cited federated learning paper (11000+ citations).

## Comparison with the state of the art

The conceptual foundation that this KB's other Federated_Learning anchors — [[2019_Wang_AdaptiveFederatedLearningEdgeComputing]], [[2021_Imteaj_FederatedLearningResourceConstrainedIoTSurvey]], and the existing [[2022_Freitag_OnDeviceTrainingMCUFederated]] — all implicitly build on (all describe horizontal FL specifically).

## Strengths

Extraordinarily influential (the field's most-cited paper); clear, durable taxonomy still in active use seven years later; directly addresses privacy, a first-order concern for any real-world federated deployment.

## Weaknesses

As a foundational/conceptual paper it predates and does not address resource-constrained edge/IoT deployment specifics, which this KB's other Federated_Learning anchors cover.

## Limitations

No empirical benchmarking of the proposed architectures on constrained hardware; the framework is deliberately general rather than deployment-specific.

## Open questions

How well does the vertical/transfer federated learning taxonomy apply to genuinely resource-constrained TinyML settings, where this KB's existing anchors focus almost exclusively on the horizontal case?

## Possible extensions

Extending this KB's Federated_Learning coverage to vertical or federated-transfer-learning scenarios specifically for TinyML/embedded deployment, an angle not yet represented among this KB's key papers.

## Relevance to our research

The single most foundational, most-cited paper in the entire field this KB's Federated_Learning concept is organized around — a striking gap this historical audit closes.

## Possible thesis topics

Surveying whether any published TinyML/embedded federated learning work uses the vertical or transfer settings this paper defines, versus the horizontal setting nearly all existing work (including this KB's own anchors) assumes.

## Possible collaborations

None specific — a foundational conceptual reference rather than an active research group.

## Links to related papers

[[2019_Wang_AdaptiveFederatedLearningEdgeComputing]], [[2021_Imteaj_FederatedLearningResourceConstrainedIoTSurvey]], [[2022_Freitag_OnDeviceTrainingMCUFederated]]
