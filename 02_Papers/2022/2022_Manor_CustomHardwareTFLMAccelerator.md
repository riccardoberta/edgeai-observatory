# Custom Hardware Inference Accelerator for TensorFlow Lite for Microcontrollers

**Full citation:** Manor, E., Greenberg, S. (2022). Custom Hardware Inference Accelerator for TensorFlow Lite for Microcontrollers. IEEE Access, 10, 73484–73493. DOI: 10.1109/ACCESS.2022.3189776

**PDF:** [IEEE Access (open access)](https://ieeexplore.ieee.org/document/9825651/)

**Verification note:** IEEE Access is a fully open-access IEEE journal; bibliographic details confirmed via WebSearch cross-referencing the Ben-Gurion University research portal and IEEE Xplore listing. Abstract-level verified via search; full IEEE-formatted text not fetched directly in this session.

**Linked concepts:** [[TensorFlow_Lite_Micro]], [[NPU]]

## Abstract summary

Presents an efficient hardware-software framework that accelerates TensorFlow Lite Micro (TFLM) inference by pairing a modified TFLM software stack running on a microcontroller with a dedicated custom neural processing unit hardware accelerator (referred to as MCU-NPU). Experimental results demonstrate up to 724x speedup compared to a pure software TFLM implementation on the same MCU.

## Research problem

TensorFlow Lite Micro's interpreter-based, software-only execution model — designed for portability across microcontrollers with no dedicated neural-computation hardware — leaves substantial performance on the table when a target device does have room for a small dedicated accelerator, but TFLM's software architecture was not originally designed with such hardware offload as a first-class integration path.

## Key idea

Modify the TFLM software stack to offload the compute-heavy kernel operations to a custom, purpose-built hardware NPU accelerator paired with the host microcontroller, rather than either running TFLM purely in software (as originally designed) or abandoning TFLM's portable software ecosystem entirely for a fully custom inference stack.

## Technical contribution

A modified TFLM software stack plus a custom MCU-NPU hardware accelerator design, integrated as a combined hardware-software system, demonstrating up to 724x inference speedup over pure-software TFLM execution on the same class of microcontroller.

## Experimental methodology

Implementation of the modified TFLM-plus-MCU-NPU system and benchmarking against a pure-software TFLM baseline on equivalent microcontroller hardware, measuring inference speedup (per the IEEE Access paper; specific benchmark models and power/area figures not independently re-derived in this abstract-level record).

## Results

Up to 724x speedup over pure-software TFLM inference on the same microcontroller class, demonstrating that TFLM's software portability and a dedicated hardware accelerator are not mutually exclusive — TFLM can serve as the software interface layer while a custom NPU handles the compute-heavy kernels underneath.

## Comparison with the state of the art

Distinguishes itself from CMSIS-NN-style software-kernel optimization (which improves TFLM's software execution on stock Cortex-M SIMD instructions without new hardware) by instead pairing TFLM with genuinely new custom hardware, addressing this Observatory's own [[TensorFlow_Lite_Micro]] open problem about "the performance gap between the generic interpreter (TFLM) and ad-hoc compiled code" from the hardware-acceleration side rather than the compiler side (microTVM).

## Strengths

Directly closes a real performance gap in TFLM's software-only execution model while preserving its portable software interface; large, clearly demonstrated speedup (724x) makes the hardware-offload value proposition concrete; fully open-access IEEE Access publication.

## Weaknesses

Requires custom hardware (the MCU-NPU) not present on off-the-shelf microcontrollers, limiting applicability to designs where such an accelerator can actually be fabricated or integrated, unlike pure-software approaches (CMSIS-NN) or compiler-based approaches (microTVM) that work on existing silicon.

## Limitations

The 724x figure is relative to pure-software TFLM baseline and specific to this custom accelerator design; it does not directly indicate how this hardware-offload approach compares to CMSIS-NN's software-only optimization or to a commercial NPU paired with TFLM via a vendor delegate.

## Open questions

How does this custom MCU-NPU-plus-TFLM approach compare in speedup, area, and power to CMSIS-NN's software-only kernel optimization on the same baseline hardware, and to a commercial NPU (e.g. Arm Ethos-U) integrated via a TFLM hardware delegate? Could the underlying MCU-NPU design principles inform a general TFLM hardware-delegate interface rather than a one-off custom accelerator?

## Possible extensions

A three-way benchmark comparing this custom MCU-NPU-accelerated TFLM, CMSIS-NN-optimized software TFLM, and a commercial NPU-delegate-accelerated TFLM on the same models and baseline microcontroller, to place the 724x figure in context against alternative acceleration paths.

## Relevance to our research

Directly addresses this Observatory's own [[TensorFlow_Lite_Micro]] open problem about the interpreter-versus-compiled-code performance gap, offering a hardware-acceleration answer that complements the compiler-based (microTVM) and software-kernel (CMSIS-NN) answers already in this Observatory's KB.

## Possible thesis topics

Benchmarking this custom MCU-NPU-accelerated TFLM approach against CMSIS-NN-optimized software TFLM and a commercial NPU delegate on a common set of TinyML models, to determine which acceleration path offers the best speedup-per-engineering-effort trade-off.

## Possible collaborations

Groups working on custom hardware accelerators for TinyML runtimes (Ben-Gurion University, per the paper's institutional affiliation).

## Links to related papers

[[2021_David_TensorFlowLiteMicro]]
