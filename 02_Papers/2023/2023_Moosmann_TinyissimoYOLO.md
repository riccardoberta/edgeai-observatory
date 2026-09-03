# TinyissimoYOLO: A Quantized, Low-Memory Footprint, TinyML Object Detection Network for Low Power Microcontrollers

**Full citation:** Moosmann, J., Giordano, M., Vogt, C., Magno, M. (2023). TinyissimoYOLO: A Quantized, Low-Memory Footprint, TinyML Object Detection Network for Low Power Microcontrollers. arXiv:2306.00001

**PDF:** [arXiv](https://arxiv.org/abs/2306.00001)

**Linked concepts:** [[Vision]]

## Abstract summary

A quantized, 422k-parameter YOLO-family object detection network fitting under 0.5 MB of weight storage, deployed on the MAX78000 microcontroller reaching up to 180 fps at 196 µJ per inference (57% mAP on PascalVOC person/chair/car classes).

## Research problem

Real-time object detection (not just classification) typically requires far more compute and memory than microcontrollers provide, and this concept's existing efficient-architecture anchors (MobileNet, ShuffleNet, TinyNeXt) target classification rather than detection specifically.

## Key idea

Design and quantize a YOLO-family detection network specifically for the sub-0.5MB, milliwatt-power regime of microcontroller-class hardware with a CNN accelerator, rather than adapting a classification-scale detector.

## Technical contribution

A full quantized object-detection network plus its deployment pipeline and evaluation on real accelerator-equipped microcontroller hardware (MAX78000).

## Experimental methodology

Trained on PascalVOC (person, chair, car classes), deployed and measured on the MAX78000 microcontroller for frame rate, energy per inference, and mAP.

## Results

Up to 180 fps at 196 µJ per inference, 57% mAP, over 106 MAC/cycle inference efficiency — demonstrating real-time object detection is feasible within a genuinely milliwatt microcontroller power budget.

## Comparison with the state of the art

Extends this concept's efficient-architecture line (MobileNet, ShuffleNet, TinyNeXt) — all classification-focused — into object detection specifically, filling a task-type gap in this concept's coverage.

## Strengths

Real hardware validation (not simulation); genuinely microcontroller-class power budget (milliwatts); open, reproducible dataset subset.

## Weaknesses

Limited to three object classes in the reported evaluation; single hardware target (MAX78000, an accelerator-equipped MCU) limits generalization to accelerator-free microcontrollers.

## Limitations

57% mAP is modest by mobile/server-class detector standards, reflecting the genuine accuracy cost of this extreme resource envelope.

## Open questions

How does TinyissimoYOLO's accuracy/energy trade-off compare on microcontrollers without a dedicated CNN accelerator (e.g., plain Cortex-M with CMSIS-NN)?

## Possible extensions

Porting TinyissimoYOLO to a non-accelerated Cortex-M target and re-measuring the energy/accuracy trade-off, directly testing whether the reported efficiency depends on the MAX78000's dedicated accelerator.

## Relevance to our research

Fills a genuine task-type gap in this concept (object detection, not just classification) at exactly the microcontroller tier this Observatory focuses on.

## Possible thesis topics

Porting TinyissimoYOLO (or a similar compact detector) to a non-accelerated Cortex-M target with CMSIS-NN and comparing energy/accuracy against the MAX78000 results.

## Possible collaborations

ETH Zürich Center for Project Based Learning (Magno group), working on ultra-low-power embedded vision.

## Links to related papers

[[2025_Zeng_TinyNeXt]], [[2017_Howard_MobileNets]]
