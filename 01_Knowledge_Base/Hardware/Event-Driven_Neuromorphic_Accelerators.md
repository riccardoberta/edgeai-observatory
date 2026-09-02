# Event-Driven / Neuromorphic Accelerators

## Evolution of the concept

Created 2026-09-02 as part of a deliberate gap-closing pass, formalizing a taxonomy gap first flagged by the 2026-08-23 weekly digest and left open pending a second, independent anchor paper (per the same conservative bar the taxonomy has applied consistently since 2026-08-25 — see the Security branch's history for the precedent). Custom event-driven hardware processes discrete, asynchronous event streams (from event cameras or neuromorphic audio sensors) rather than the fixed-rate, dense tensors that Cortex-M/A, RISC-V, DSP, FPGA, and NPU accelerators in this taxonomy's other Hardware nodes are built around — it does not map onto any of them.

The concept's lineage starts with [[2024_Yang_EvGNN]] (Yang, Kneip, Frenkel; TU Delft, 2024), the first event-driven graph-neural-network (EV-GNN) accelerator, an FPGA design for event-camera vision. The same core author subset (Kneip, Frenkel) later scaled this to real silicon with [[2026_Kneip_ETHEREAL]] (2026), the first measured-silicon EV-GNN ASIC, extending to high (VGA-class) resolution. Both papers come from one research cluster (TU Delft/KU Leuven/UZH/Penn), so on their own they would not clear this taxonomy's two-*independent*-anchor bar for formalization — the deciding evidence is [[2026_Jeziorek_EventAudioGNNKWS]] (Jeziorek et al.; AGH University of Krakow, CEA-List, Keio University, 2026), a fully independent research group applying the same event-graph-neural-network hardware paradigm to a different sensing modality (neuromorphic audio rather than vision) and a different application (keyword spotting), on FPGA. That a second, unrelated group converged on the same architectural paradigm for a different sensor type is the strongest available evidence that event-driven graph neural hardware is a real, generalizable direction rather than one lab's specialization.

## Key papers

[[2024_Yang_EvGNN]] — first event-driven GNN accelerator (FPGA), for event-camera vision; 87.8% accuracy at 16µs/event latency on N-CARS.

[[2026_Kneip_ETHEREAL]] — first measured-silicon EV-GNN ASIC, scaling to VGA-resolution event vision; 25.6µs/inference, 1.6µJ/inference.

[[2026_Jeziorek_EventAudioGNNKWS]] — independent research group's FPGA event-graph-GNN implementation for neuromorphic audio classification and end-to-end keyword spotting; first hardware-accelerated SSC-dataset result; outperforms FPGA-based SNN baselines by up to 19.3%.

## Open problems

Does the event-graph-neural-network hardware paradigm generalize further, to biosignal spike trains, sparse radar point clouds, or other genuinely sparse, asynchronous sensor streams beyond vision and audio — a question raised independently in both the ETHEREAL and Jeziorek et al. records? How does FPGA-generation hardware (EvGNN, Jeziorek et al.) compare, under matched conditions, to ASIC-generation hardware (ETHEREAL) in latency and energy once the algorithmic workload is held constant? Is there a unifying architectural template across the vision and audio implementations, or do the two modalities require genuinely different event-graph designs?

## Research ideas

A matched-condition, cross-modality benchmark comparing the vision-domain (EvGNN/ETHEREAL) and audio-domain (Jeziorek et al.) event-graph-hardware designs on shared metrics (latency/event, energy/event, accuracy) to identify which architectural choices are modality-specific versus genuinely general. A third-modality proof of concept (biosignal event streams) to test whether the paradigm extends beyond vision and audio, as both existing paper lineages speculate but neither demonstrates.

## Possible thesis topics

A cross-modality comparative study of event-driven graph-neural-network hardware across vision (EvGNN/ETHEREAL) and audio (Jeziorek et al.) implementations, identifying shared versus modality-specific architectural principles (PhD-scale; bridges [[Vision]], [[Keyword_Spotting]], and this concept). Extending the event-graph-hardware paradigm to a third sensing modality — biosignal spike trains — as a proof-of-concept generality test (Master's/PhD; bridges [[Biosignals]] and this concept). A matched-condition ASIC-vs-FPGA efficiency comparison isolating the silicon-vs-emulation contribution from the algorithmic contribution across the EvGNN-to-ETHEREAL lineage (Master's).

## Links

[[Vision]], [[Keyword_Spotting]], [[Biosignals]], [[FPGA]], [[Quantization]]
