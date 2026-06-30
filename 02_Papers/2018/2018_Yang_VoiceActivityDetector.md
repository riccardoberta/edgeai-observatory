# A 1μW Voice Activity Detector Using Analog Feature Extraction and Digital Deep Neural Network

**Full citation:** Yang, M., Yeh, C.H., Zhou, J., Cerqueira, J.P., Lazar, A.A., Seok, M. (2018). A 1μW Voice Activity Detector Using Analog Feature Extraction and Digital Deep Neural Network. *IEEE International Solid-State Circuits Conference (ISSCC 2018)*. https://ieeexplore.ieee.org/document/8310326/

**Linked concepts:** [[DSP]]

## Abstract summary

The authors present a voice activity detection (VAD) chip that combines an analog front end for feature extraction with a small digital deep neural network classifier, achieving voice activity detection at approximately 1 microwatt of power consumption — orders of magnitude below typical fully-digital always-on audio processing pipelines.

## Research problem

Always-on voice activity detection (deciding whether a microphone signal currently contains speech, to gate more expensive downstream processing such as keyword spotting or speech recognition) must run continuously on a battery-powered device, but fully-digital signal-processing-plus-DNN pipelines consume far more power than a true always-on, battery-friendly system can afford.

## Key idea

Move the most power-hungry stage of the pipeline — continuous feature extraction from the raw analog microphone signal — into the analog domain, where it can be performed at a fraction of the energy cost of digitizing and digitally processing the full audio stream; only the already-extracted, much lower-bandwidth features are passed to a small digital DNN classifier for the final speech/non-speech decision.

## Technical contribution

A complete analog-feature-extraction-plus-digital-DNN-classifier chip architecture and circuit implementation; a demonstration that splitting the signal-processing pipeline at the analog/digital boundary in this way can reduce always-on VAD power consumption to roughly microwatt levels, a regime unreachable by purely digital implementations of comparable accuracy.

## Experimental methodology

Implements and fabricates the analog-feature-extraction circuit and digital DNN classifier as a single chip, characterizing actual measured power consumption and voice-activity-detection accuracy on real audio test data, and comparing against fully-digital VAD implementations of similar accuracy.

## Results

Achieves voice activity detection accuracy competitive with digital VAD baselines while consuming approximately 1 microwatt of power, a substantial (orders-of-magnitude) reduction compared to typical fully-digital always-on audio processing pipelines of similar function.

## Comparison with the state of the art

Demonstrates a power efficiency level not achievable by digital-only signal-processing-plus-DNN pipelines of the time, establishing analog/digital co-design as a viable strategy specifically for the always-on, ultra-low-power tier of an audio processing pipeline, ahead of more expensive (but more flexible) digital keyword-spotting stages.

## Strengths

A concrete, fabricated, measured demonstration (not just a simulation) that analog front-end processing can deliver order-of-magnitude power savings for always-on sensing tasks while retaining DNN-level classification accuracy in the digital back end.

## Weaknesses

Analog circuits are less flexible and reprogrammable than digital signal processing, and are sensitive to process variation, temperature, and supply-voltage noise; the feature set extracted by the analog front end is fixed by the circuit design, which limits adaptability to new tasks compared to a fully digital, software-configurable pipeline.

## Limitations

Demonstrated specifically for a binary voice-activity-detection task rather than the full speech-recognition or keyword-spotting pipelines that typically follow it; generalizing the same analog-feature-extraction philosophy to more complex always-on audio classification tasks (e.g. multi-keyword spotting) is not addressed.

## Open questions

How far can the analog-front-end approach be extended toward more complex always-on audio classification tasks (e.g. small-vocabulary keyword spotting) while retaining microwatt-level power consumption? How should the analog/digital boundary be chosen to balance flexibility against power efficiency for a given task?

## Possible extensions

Extending analog-front-end feature extraction beyond binary VAD toward small-vocabulary keyword spotting, co-designed with the small-footprint CNN architectures explored in [[2015_Sainath_CNNKeywordSpotting]], to push the entire always-on detection stage further into the microwatt power regime.

## Relevance to our research

An early, concrete instance of signal-processing/learned-classifier co-design for ultra-low-power always-on audio sensing, directly relevant to the [[DSP]] and [[Keyword_Spotting]] research directions whenever extreme power efficiency is the binding constraint.

## Possible thesis topics

A feasibility study extending the analog-feature-extraction-plus-digital-DNN approach from binary voice activity detection to a small multi-keyword classification task, characterizing the resulting power/accuracy trade-off relative to a fully-digital small-footprint CNN baseline.

## Possible collaborations

Mixed-signal/analog circuit design groups and researchers working on always-on, ultra-low-power audio sensing pipelines.

## Links to related papers

[[2015_Sainath_CNNKeywordSpotting]]
