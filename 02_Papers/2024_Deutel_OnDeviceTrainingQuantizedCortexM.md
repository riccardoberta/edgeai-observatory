# On-Device Training of Fully Quantized Deep Neural Networks on Cortex-M Microcontrollers

**Full citation:** Deutel, M., Hannig, F., Mutschler, C., Teich, J. (2024). On-Device Training of Fully Quantized Deep Neural Networks on Cortex-M Microcontrollers. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 44(4), 1250-1261. arXiv:2407.10734. https://arxiv.org/abs/2407.10734

**Linked concepts:** [[Cortex-M]], [[On-device_Learning]], [[Quantization]]

## Abstract summary

The authors (Fraunhofer IIS / FAU Erlangen-Nürnberg) present a method for training deep neural networks entirely in place on Cortex-M microcontrollers, using fully quantized training (FQT) combined with dynamic partial gradient updates, and evaluate feasibility and resource trade-offs across Cortex-M0+, Cortex-M4, and Cortex-M7 targets.

## Research problem

DNN training is resource-intensive (memory, compute, floating-point support) and conventionally assumed to require a server or at least a capable edge device; enabling adaptation/fine-tuning directly on a microcontroller, without offloading to the cloud, remains largely unsolved for the most constrained Cortex-M class of hardware.

## Key idea

Keep the entire training loop — forward pass, backward pass, and weight updates — in a fully quantized integer representation, and dynamically select only a subset of gradients/parameters to update at each step to fit within the MCU's tight memory and compute budget.

## Technical contribution

A fully quantized training (FQT) scheme compatible with Cortex-M's lack of efficient floating-point support; a dynamic partial gradient update mechanism that trades off how much of the network is updated against available memory/compute, instead of a fixed, hand-tuned subset.

## Experimental methodology

Evaluation on multiple vision and time-series datasets, training/fine-tuning models directly on three Cortex-M variants (M0+, M4, M7) spanning a wide range of available compute and memory, measuring achievable accuracy alongside memory footprint, training time, and energy.

## Results

The method demonstrates that on-device training of quantized DNNs is feasible even on the most constrained Cortex-M0+ target, with accuracy trade-offs and resource costs that scale predictably with the amount of compute/memory available on each MCU tier.

## Comparison with the state of the art

Most prior MCU-targeted work (CMSIS-NN, TensorFlow Lite Micro) addresses only inference; this work extends the on-device envelope to training itself, complementing the broader [[On-device_Learning]] literature that has mostly targeted less constrained microprocessor-class hardware.

## Strengths

Spans three meaningfully different Cortex-M tiers rather than a single MCU; directly measures the practical resource cost of on-device training rather than only its feasibility in principle.

## Weaknesses

Training cost (time, energy) on the most constrained tier (Cortex-M0+) remains substantial relative to a single inference pass, limiting how often such on-device updates can realistically occur in a battery-powered deployment.

## Limitations

Evaluated on vision and time-series tasks of moderate complexity; scaling to larger models or to continual/streaming training scenarios (cf. [[Continual_Learning]]) is not directly addressed.

## Open questions

How does dynamic partial gradient update selection interact with catastrophic forgetting when training continues over many on-device updates? Can the same FQT approach extend efficiently to Cortex-M cores with Helium (MVE) vector instructions?

## Possible extensions

Combining this FQT/partial-update approach with a continual-learning-aware update schedule; porting the scheme to RISC-V microcontroller targets for a cross-ISA comparison.

## Relevance to our research

Directly extends the Cortex-M hardware target — otherwise mostly an inference-only platform in our taxonomy — to cover on-device training, connecting [[Cortex-M]] to [[On-device_Learning]] with a concrete, hardware-validated method.

## Possible thesis topics

Benchmarking this FQT approach against alternative on-device training methods (e.g. TinyTrain) on a common Cortex-M target and task; extending dynamic partial gradient updates to a Helium-accelerated Cortex-M55/M85 target.

## Possible collaborations

Groups working on on-device learning frameworks (TinyTrain) and on Cortex-M kernel libraries (CMSIS-NN) that could supply optimized quantized training primitives.

## Links to related papers

[[2018_Lai_CMSIS-NN]], [[2024_Kwon_TinyTrain]]
