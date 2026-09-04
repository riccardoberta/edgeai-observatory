# Event-Driven / Neuromorphic Accelerators

Custom event-driven hardware processes discrete, asynchronous event streams — from event cameras or neuromorphic audio sensors, which report only *changes* in the input rather than a full frame or sample window at fixed intervals — instead of the fixed-rate, dense tensors that Cortex-M/A, RISC-V, DSP, FPGA, and NPU accelerators are built around. This suits sparse, asynchronous sensor data and does not map onto any of this taxonomy's other Hardware concepts.

## Evolution of the concept

The concept's lineage starts with Yang, Kneip, and Frenkel's EvGNN (2024), the first event-driven graph-neural-network (EV-GNN) accelerator: an FPGA design for event-camera vision. The same core authors later scaled this to real silicon with Kneip's ETHEREAL (2026), the first measured-silicon EV-GNN application-specific integrated circuit (ASIC), extending to high (VGA-class) resolution.

Both of those papers come from one research cluster (TU Delft/KU Leuven/UZH/Penn). Independent corroboration that this is a real, generalizable architectural direction — not one lab's specialization — comes from Jeziorek et al. (2026), a fully unrelated research group (AGH University of Kraków, CEA-List, Keio University) applying the same event-graph-neural-network hardware paradigm to a different sensing modality (neuromorphic audio rather than vision) and a different application (keyword spotting), also on FPGA. That a second, unrelated group converged on the same architectural paradigm for a different sensor type is the strongest available evidence that event-driven graph neural hardware generalizes beyond a single group's work.

## Key papers

[[2024_Yang_EvGNN]] — first event-driven graph-neural-network accelerator (FPGA), for event-camera vision; 87.8% accuracy at 16µs/event latency on the N-CARS dataset.

[[2026_Kneip_ETHEREAL]] — first measured-silicon event-driven graph-neural-network application-specific integrated circuit, scaling to VGA-resolution event vision; 25.6µs/inference, 1.6µJ/inference.

[[2026_Jeziorek_EventAudioGNNKWS]] — an independent research group's FPGA event-graph-neural-network implementation for neuromorphic audio classification and end-to-end keyword spotting; outperforms FPGA-based spiking-neural-network baselines by up to 19.3%.

## Open problems

Does the event-graph-neural-network hardware paradigm generalize further, to biosignal spike trains, sparse radar point clouds, or other genuinely sparse, asynchronous sensor streams beyond vision and audio — a question raised independently by both the ETHEREAL and Jeziorek et al. papers? How does FPGA-generation hardware (EvGNN, Jeziorek et al.) compare, under matched conditions, to application-specific-integrated-circuit-generation hardware (ETHEREAL) in latency and energy once the algorithmic workload is held constant? Is there a unifying architectural template across the vision and audio implementations, or do the two modalities require genuinely different event-graph designs?

## Research ideas

A matched-condition, cross-modality benchmark comparing the vision-domain (EvGNN/ETHEREAL) and audio-domain (Jeziorek et al.) event-graph-hardware designs on shared metrics (latency/event, energy/event, accuracy) to identify which architectural choices are modality-specific versus genuinely general. A third-modality proof of concept (biosignal event streams) to test whether the paradigm extends beyond vision and audio, as both existing paper lineages speculate but neither demonstrates.

## Possible thesis topics

A cross-modality comparative study of event-driven graph-neural-network hardware across vision (EvGNN/ETHEREAL) and audio (Jeziorek et al.) implementations, identifying shared versus modality-specific architectural principles (PhD-scale; bridges [[Vision]], [[Keyword_Spotting]], and this concept). Extending the event-graph-hardware paradigm to a third sensing modality — biosignal spike trains — as a proof-of-concept generality test (Master's/PhD; bridges [[Biosignals]] and this concept). A matched-condition ASIC-versus-FPGA efficiency comparison isolating the silicon-versus-emulation contribution from the algorithmic contribution across the EvGNN-to-ETHEREAL lineage (Master's).

## Links

[[Vision]], [[Keyword_Spotting]], [[Biosignals]], [[FPGA]], [[Quantization]]
