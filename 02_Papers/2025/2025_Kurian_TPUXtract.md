# TPUXtract: An Exhaustive Hyperparameter Extraction Framework

**Full citation:** Kurian, A., Dubey, A., Yaman, F., Aysu, A. (2025). TPUXtract: An Exhaustive Hyperparameter Extraction Framework. IACR Transactions on Cryptographic Hardware and Embedded Systems, 2025(1), 78-103.

**PDF:** [IACR TCHES](https://tches.iacr.org/index.php/TCHES/article/view/11923)

**Linked concepts:** [[Hardware_Security_of_Edge_AI_Accelerators]]

## Abstract summary

The first successful model extraction attack on the commercially available Google Edge TPU, using electromagnetic traces and an online template-building approach (rather than a pre-trained ML-based approach) to extract complete layer configurations — type, node count, kernel/filter sizes, filter count, strides, padding, activation function — with 99.91% accuracy, even for previously unseen models.

## Research problem

Prior neural-architecture-extraction attacks (following the [[2019_Batina_CSINN]] paradigm) had not been demonstrated against a real, commercially deployed edge AI accelerator; whether the same EM-extraction threat model applies to production edge hardware like the Google Edge TPU was untested.

## Key idea

Build extraction templates online (during the attack itself) rather than relying on a pre-trained ML classifier for trace interpretation, making the attack generalize to previously unseen model architectures rather than only ones represented in a training set.

## Technical contribution

The first demonstrated end-to-end model extraction attack against the Google Edge TPU specifically; an online template-building extraction methodology achieving markedly higher accuracy (99.91%) than prior ML-classifier-based approaches.

## Experimental methodology

EM trace collection from a physical Google Edge TPU during inference, hyperparameter extraction via online template building, validated against both known and previously-unseen model architectures.

## Results

99.91% extraction accuracy — the most accurate hyperparameter-extraction attack reported to date — and the first to generalize to previously-unseen architectures rather than requiring pre-training on the target architecture family.

## Comparison with the state of the art

Direct methodological descendant of [[2019_Batina_CSINN]]'s EM-extraction paradigm, but the first to target a specific, commercially deployed edge accelerator (Google Edge TPU) rather than a research microcontroller setup — closing the gap between this concept's foundational threat model and its real-hardware relevance.

## Strengths

Real commercial hardware target (not a research prototype); highest reported accuracy in the extraction literature; generalizes to unseen architectures via online template building rather than requiring pre-training.

## Weaknesses

Single hardware target (Google Edge TPU); requires physical EM measurement access, the same practical constraint as CSI NN.

## Limitations

Extracts hyperparameters/architecture, not weights directly (a distinct but related threat from LLMscope's weight/activation extraction).

## Open questions

Does TPUXtract's online template-building approach generalize to other commercial edge accelerators (NPUs, custom ASICs) beyond the Google Edge TPU, and how does its accuracy compare against LLMscope's laser-voltage-imaging approach for the overlapping goal of model-asset extraction?

## Possible extensions

Applying TPUXtract's online template-building methodology to a second commercial edge accelerator family, testing whether the 99.91% accuracy and unseen-architecture generalization hold beyond the Edge TPU.

## Relevance to our research

The most concrete, hardware-specific demonstration yet that this concept's physical-extraction threat model applies to real, commercially deployed edge AI accelerators, not just research prototypes — directly relevant given this Observatory's own NPU/Edge-TPU-tracking anchors ([[2021_Yazdanbakhsh_EdgeTPUEvaluation]]).

## Possible thesis topics

Extending TPUXtract's online template-building extraction methodology to a second commercial edge accelerator (e.g. an ARM Ethos NPU or a RISC-V NPU) and comparing accuracy/cost against the reported Edge TPU results.

## Possible collaborations

North Carolina State University (Aysu group) — hardware security for ML accelerators.

## Links to related papers

[[2019_Batina_CSINN]], [[2026_Mehta_LLMscope]], [[2021_Yazdanbakhsh_EdgeTPUEvaluation]]
