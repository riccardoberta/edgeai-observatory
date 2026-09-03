# CSI NN: Reverse Engineering of Neural Network Architectures Through Electromagnetic Side Channel

**Full citation:** Batina, L., Bhasin, S., Jap, D., Picek, S. (2019). CSI NN: Reverse Engineering of Neural Network Architectures Through Electromagnetic Side Channel. 28th USENIX Security Symposium, 515-532.

**PDF:** [USENIX](https://www.usenix.org/system/files/sec19-batina.pdf)

**Linked concepts:** [[Hardware_Security_of_Edge_AI_Accelerators]]

## Abstract summary

The foundational demonstration that a neural network's full architecture (layer count, layer types, number of neurons, activation functions) can be reverse-engineered from electromagnetic emanations recorded during inference on a microcontroller, without any logical/software access to the model.

## Research problem

Deploying a proprietary neural network on embedded hardware was assumed to protect the model's architecture as intellectual property, since there was no established attack demonstrating that EM emanations alone could reveal it.

## Key idea

Correlate electromagnetic side-channel traces recorded during inference with candidate architectural choices (layer type, neuron count, activation function), building up a full architecture reconstruction one architectural decision at a time from physical measurements alone.

## Technical contribution

The first end-to-end EM-side-channel neural architecture extraction methodology, later cited by essentially every subsequent paper in this concept's physical-extraction threat model, including this concept's own LLMscope anchor.

## Experimental methodology

EM traces captured during inference on microcontroller-class hardware running known reference architectures, with the extraction methodology validated by successfully reconstructing several standard architectures from the traces alone.

## Results

Successfully reconstructed full neural network architectures (layer types, counts, sizes, activation functions) purely from EM side-channel measurements, establishing model architecture as a genuine physical-security asset requiring protection.

## Comparison with the state of the art

The founding paper of this concept's entire physical/side-channel-extraction threat model — directly preceding and enabling [[2026_Mehta_LLMscope]]'s laser-voltage-imaging extraction and complementing [[2022_Dubey_GuardingMLHardwareSideChannel]]'s power/EM survey coverage, both of which build on the extraction paradigm this paper established.

## Strengths

Extraordinarily influential (450+ citations) founding paper of an entire attack-class; methodologically rigorous validation against known reference architectures; demonstrates a genuinely novel threat (architecture, not just data, is extractable).

## Weaknesses

Validated on relatively simple microcontroller-hosted networks by modern standards; does not address weight/activation extraction (architecture reconstruction only), which later papers (including LLMscope) extend to.

## Limitations

Requires physical proximity for EM measurement; countermeasure evaluation not central to the paper's own scope.

## Open questions

How does EM-based architecture extraction scale to the LLM/MoE-class models this concept's more recent anchors ([[2026_Mehta_LLMscope]], [[2026_Fang_YAVIN]]) address, given their vastly larger architecture search space?

## Possible extensions

Extending CSI NN's EM-based architecture-extraction methodology to modern edge-LLM accelerators, testing whether the same correlation-based approach scales to transformer/MoE architectural choices.

## Relevance to our research

The founding paper of this concept's entire physical-extraction research thread — a significant gap given the concept's two 2026 anchors are direct methodological descendants of this 2019 work without citing it.

## Possible thesis topics

Reproducing CSI NN's EM-extraction methodology against a modern edge NPU or TPU, comparing recovery accuracy and cost against TPUXtract's later, more automated approach.

## Possible collaborations

Radboud University / TU Delft / NTU Singapore (Batina, Bhasin, Picek group) — foundational hardware-security-for-ML research groups.

## Links to related papers

[[2026_Mehta_LLMscope]], [[2022_Dubey_GuardingMLHardwareSideChannel]]
