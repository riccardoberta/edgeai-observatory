# Hardware-Friendly and Efficient Vision Transformer for Deployment on Low-Power Embedded Device

**Full citation:** Zhang, M. (2026). Hardware-Friendly and Efficient Vision Transformer for Deployment on Low-Power Embedded Device. Journal of Low Power Electronics and Applications, 16(1), 1. DOI: 10.3390/jlpea16010001

**PDF:** [MDPI (open access)](https://www.mdpi.com/2079-9268/16/1/1)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Vision]], [[NAS]]

## Abstract summary

Proposes a hardware-friendly CNN-Transformer hybrid pyramid architecture for embedded vision, integrating convolutional bottlenecks with Transformer encoders to capture local and global context at low computational cost. Redesigns key nonlinear operations that are hardware-unfriendly on embedded platforms — replacing GELU and Layer Normalization with ReLU and Batch Normalization, and introducing "Softmax2," a simplified logarithmic-exponential Softmax approximation that eliminates costly exponential/division operations — while adding a pyramid feature-extraction structure for multi-scale semantic representation.

## Research problem

Vision Transformers achieve strong accuracy via global dependency modeling but rely on operations (Layer Normalization, Softmax, GELU) that are computationally expensive and hardware-unfriendly to implement efficiently on resource-constrained embedded platforms, severely limiting real deployment despite the architecture's representational advantages.

## Key idea

Keep the Transformer's global-context-modeling benefit but replace its most hardware-costly nonlinear components with hardware-friendly approximations (ReLU for GELU, Batch Normalization for Layer Normalization, and a simplified logarithmic-exponential "Softmax2" that avoids expensive exponential/division operations), combined with a CNN-Transformer hybrid pyramid structure that keeps overall computational cost low.

## Technical contribution

A hardware-friendly CNN-Transformer hybrid pyramid architecture for embedded vision, with three specific hardware-motivated component redesigns (ReLU-for-GELU, BN-for-LN, and the Softmax2 approximation) validated as a combined system rather than proposed only individually.

## Experimental methodology

Architecture design and experimental evaluation of the CNN-Transformer hybrid pyramid model with the hardware-friendly component substitutions, assessing accuracy, computational cost, and deployability for real-time embedded vision applications (per the MDPI article; specific benchmark datasets and quantitative accuracy/latency figures not independently re-derived in this record).

## Results

The proposed architecture and its hardware-friendly nonlinear-operation redesigns demonstrate a practical balance of accuracy, efficiency, and deployability, validated as offering a promising solution for real-time and embedded vision applications (per the published abstract).

## Comparison with the state of the art

Extends this Observatory's [[Vision]] concept's efficient-architecture lineage — from MobileNet's depthwise-separable convolutions through [[2025_Zeng_TinyNeXt]]'s memory-efficient self-attention — by attacking a different bottleneck: not the attention mechanism's memory footprint itself, but the hardware cost of the surrounding nonlinear operations (LN, Softmax, GELU) that TinyNeXt-style efficient-attention designs still typically retain.

## Strengths

Targets a genuinely under-addressed bottleneck (hardware-unfriendly nonlinear operations) rather than only parameter count or FLOPs; combines multiple complementary hardware-motivated redesigns (activation, normalization, Softmax) into one validated system; fully open-access, full-text-verifiable.

## Weaknesses

As an abstract-level record for a very recently published (Dec 2025/2026) paper, specific quantitative accuracy-retention figures for the ReLU/BN/Softmax2 substitutions relative to standard GELU/LN/Softmax are not captured here beyond the general claim of a "promising and practical" trade-off.

## Limitations

Hardware-friendly approximations (ReLU, BN, Softmax2) may trade some accuracy for efficiency relative to the original GELU/LN/Softmax formulation; the paper's target hardware class (which specific low-power embedded platforms) is not detailed in this record.

## Open questions

How much accuracy is actually traded for the Softmax2/ReLU/BN substitutions relative to standard Transformer nonlinearities, and does this trade-off hold across different vision tasks (classification vs. detection)? How does this hardware-friendly hybrid architecture compare directly, on the same benchmark and target hardware, to [[2025_Zeng_TinyNeXt]]'s Lean Single-Head Self-Attention approach?

## Possible extensions

A direct, controlled comparison of this paper's hardware-friendly-nonlinearity approach against [[2025_Zeng_TinyNeXt]]'s memory-efficient-attention approach on the same embedded vision benchmark, to determine whether the two efficiency strategies (nonlinearity redesign vs. attention redesign) compose or substitute for each other.

## Relevance to our research

Extends this Observatory's [[Vision]] concept's efficient-by-design architecture lineage with a hardware-nonlinearity-focused strategy distinct from [[2025_Zeng_TinyNeXt]]'s attention-memory-focused strategy, broadening the concept's coverage of what "efficient" means for embedded vision transformers.

## Possible thesis topics

Benchmarking this paper's hardware-friendly nonlinearity substitutions (Softmax2, ReLU, BN) combined with [[2025_Zeng_TinyNeXt]]'s memory-efficient attention on the same embedded vision task, to test whether the two efficiency strategies compose for a larger combined gain than either alone.

## Possible collaborations

Groups working on hardware-aware vision transformer design and low-power embedded vision deployment.

## Links to related papers

[[2025_Zeng_TinyNeXt]]
