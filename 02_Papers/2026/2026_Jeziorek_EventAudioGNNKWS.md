# Hardware-accelerated graph neural networks: an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA

**Full citation:** Jeziorek, K., Wzorek, P., Blachut, K., Nakano, H., Dampfhoffer, M., Mesquida, T., Nishi, H., Dalgaty, T., Kryjak, T. (2026). Hardware-accelerated graph neural networks: an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA. arXiv:2602.16442 [cs.LG, cs.AI, cs.SD, eess.AS]. AGH University of Krakow; CEA-List; Keio University. Submitted 18 Feb 2026. Under revision, ACM Transactions on Reconfigurable Technology and Systems (TRETS). DOI: 10.48550/arXiv.2602.16442.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2602.16442)

**Linked concepts:** [[Event-Driven_Neuromorphic_Accelerators]], [[Keyword_Spotting]], [[FPGA]]

## Abstract summary

Neuromorphic sensors (here, an artificial cochlea) produce sparse, discrete audio event streams that conventional dense neural architectures handle inefficiently. The paper presents an FPGA implementation of event-driven graph neural networks (GNNs) for audio processing, converting cochlea output into sparse event-graph data. Evaluated on the Spiking Heidelberg Digits (SHD) and Spiking Speech Commands (SSC) datasets, the floating-point model reaches 92.7% accuracy on SHD — 2.4 points below the state of the art — with over 10x and 67x fewer parameters, and the quantised model outperforms FPGA-based spiking neural network baselines by up to 19.3%. The paper also demonstrates the first end-to-end FPGA event-audio keyword-spotting system, combining graph convolution with recurrent sequence modelling, reaching up to 95% word-end detection accuracy at 10.53µs latency and 1.18W power.

## Research problem

Neuromorphic audio sensors (artificial cochleae) generate sparse, asynchronous event streams rather than dense fixed-rate audio frames, but most deployed keyword-spotting and audio-classification pipelines are built around dense architectures (CNNs, RNNs) that do not exploit this sparsity. Spiking neural networks (SNNs) are the traditional match for event data but historically trail non-spiking approaches in accuracy; there was also, until this work, no complete FPGA implementation combining event-graph representation with the temporal sequence modelling that real keyword spotting (not just isolated-digit classification) requires.

## Key idea

Represent the cochlea's event stream as a graph (following the event-graph-neural-network paradigm already used for event-camera vision, e.g. [[2024_Yang_EvGNN]] and [[2026_Kneip_ETHEREAL]]) and process it with a hardware-accelerated GNN on an SoC FPGA, rather than a spiking or dense-recurrent network. For the full keyword-spotting task, the graph-convolutional event encoder is paired with a recurrent sequence-modelling stage so the system can detect word boundaries in a continuous stream, not just classify pre-segmented isolated events.

## Technical contribution

(1) An FPGA implementation of event-graph neural networks applied to audio for the first time (prior event-GNN hardware work targeted vision); (2) a systematic comparison against FPGA-based spiking neural network baselines on the same datasets; (3) the first hardware-accelerated evaluation reported on the SSC (Spiking Speech Commands) dataset; (4) the first end-to-end FPGA implementation of event-audio keyword spotting, combining graph convolution with recurrent sequence modelling for continuous-stream word-end detection.

## Experimental methodology

Implemented on a SoC FPGA (device not confirmed at abstract level; verify from full PDF). Evaluated on two open-source neuromorphic audio datasets: SHD (Spiking Heidelberg Digits, isolated-digit classification) and SSC (Spiking Speech Commands, a larger vocabulary). Compared a floating-point baseline model against a quantised deployment model, and against FPGA-based SNN baselines from prior work. The keyword-spotting system was evaluated end-to-end for continuous-stream word-end detection latency and power.

## Results

92.7% accuracy on SHD (2.4 points below the state of the art) with over 10x and 67x fewer parameters than compared baselines. 66.9–71.0% accuracy on SSC — reported as the first hardware-accelerated evaluation on this dataset. The quantised model reaches 92.3% accuracy, outperforming FPGA-based SNN baselines by up to 19.3% while using fewer resources and lower latency. The end-to-end keyword-spotting system reaches up to 95% word-end detection accuracy at 10.53µs latency and 1.18W power.

## Comparison with the state of the art

Positioned directly against FPGA-based spiking neural network accelerators — the traditional hardware match for event data — and shown to outperform them by up to 19.3% in accuracy at lower resource cost and latency, while trailing the (presumably non-hardware-constrained) software state of the art on SHD by only 2.4 points. Extends the event-graph-neural-network hardware paradigm, previously validated only on event-camera vision ([[2024_Yang_EvGNN]], [[2026_Kneip_ETHEREAL]]), into the audio domain — independent confirmation that the approach generalizes across sensing modalities, from an entirely different research group than the vision-side EvGNN/ETHEREAL work (AGH Kraków, CEA-List, and Keio, versus TU Delft/KU Leuven/UZH/Penn).

## Strengths

Genuinely independent cross-modality validation of the event-graph-neural-network hardware approach (audio rather than vision), strengthening the case that this is a real, generalizable hardware paradigm rather than a vision-specific trick; first hardware-accelerated SSC result, giving the field a new reference point; the end-to-end KWS system (not just isolated-event classification) demonstrates practical relevance for real always-on audio sensing; microsecond-scale latency and sub-2W power are compatible with genuinely constrained edge deployment.

## Weaknesses

Still under revision (not yet accepted at TRETS as of this record), so results have not cleared full peer review; trails the software state of the art on SHD by 2.4 points, and the paper does not report on more realistic, noisier acoustic conditions beyond the two benchmark datasets; FPGA device, process node, and full resource-utilization breakdown not confirmed from abstract-level material — needs full-PDF verification.

## Limitations

Evaluated only on two neuromorphic audio benchmark datasets (SHD, SSC), both derived from broadly clean recording conditions rather than real-world noisy environments; requires a neuromorphic cochlea front-end to produce the event stream in the first place, which is a less mature and less widely deployed sensing modality than conventional microphones paired with MFCC front-ends (the more standard [[Keyword_Spotting]] pipeline, per [[2025_Bartoli_EndToEndKeywordSpotting]]).

## Open questions

Does the event-graph-GNN approach extend to other sparse sensing modalities beyond vision and audio — e.g. biosignals, as ETHEREAL's own record already speculates? How does the end-to-end KWS system perform under realistic acoustic noise and multi-speaker conditions, an open problem this Observatory's [[Keyword_Spotting]] concept already tracks for the conventional MFCC-based pipeline? What is the practical deployment cost of the artificial-cochlea front-end itself, relative to a conventional microphone+MFCC pipeline?

## Possible extensions

A direct efficiency and accuracy comparison between this event-graph audio pipeline and the conventional MFCC/CNN keyword-spotting pipeline already tracked in [[Keyword_Spotting]] ([[2025_Bartoli_EndToEndKeywordSpotting]]), on equivalent hardware; evaluation under added background noise, mirroring the research idea already proposed for the conventional KWS pipeline; extending the event-graph approach to other biosignal or sensor-fusion audio tasks.

## Relevance to our research

Provides the second, genuinely independent anchor paper for a new [[Event-Driven_Neuromorphic_Accelerators]] Hardware taxonomy node — until this record, the Observatory's only event-driven-GNN-hardware evidence was a single research cluster's vision work (EvGNN, ETHEREAL). Also bridges into [[Keyword_Spotting]] as a structurally different, neuromorphic-sensor-based alternative to the Observatory's existing MFCC/CNN keyword-spotting literature.

## Possible thesis topics

A head-to-head efficiency/accuracy/latency comparison of this event-graph audio-KWS pipeline against the conventional MFCC+CNN pipeline in [[Keyword_Spotting]] on equivalent constrained hardware (Master's; bridges Applications and Hardware). Extending event-graph neural hardware to a third sensing modality (biosignals) to test generality across all three senses this Observatory tracks (PhD-scale).

## Possible collaborations

The AGH University of Krakow / CEA-List / Keio University author team for neuromorphic audio and event-graph hardware; natural companion collaboration with the TU Delft/KU Leuven/UZH group behind [[2024_Yang_EvGNN]] and [[2026_Kneip_ETHEREAL]] for a cross-modality event-graph-hardware comparison study.

## Links to related papers

[[2024_Yang_EvGNN]] and [[2026_Kneip_ETHEREAL]] (event-driven GNN hardware for vision — the prior-art lineage this paper extends into audio); [[2025_Bartoli_EndToEndKeywordSpotting]] (the Observatory's existing conventional-pipeline keyword-spotting benchmark, a natural comparison point).
