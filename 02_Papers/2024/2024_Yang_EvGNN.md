# EvGNN: An Event-driven Graph Neural Network Accelerator for Edge Vision

**Full citation:** Yang, Y., Kneip, A., Frenkel, C. (2024). EvGNN: An Event-driven Graph Neural Network Accelerator for Edge Vision. arXiv:2404.19489 [cs.CV, cs.AR, cs.ET, cs.NE]. Delft University of Technology. Submitted 30 Apr 2024, revised 28 Feb 2025. Accepted for publication in IEEE Transactions on Circuits and Systems for Artificial Intelligence, 2025. DOI: 10.1109/TCASAI.2024.3520905.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2404.19489)

**Linked concepts:** [[Event-Driven_Neuromorphic_Accelerators]], [[Vision]], [[FPGA]]

## Abstract summary

Event-based cameras deliver microsecond-scale temporal resolution with sparse information encoding, but mainstream frame-based vision algorithms (CNNs) are optimized for dense matrix-vector multiplication and cannot exploit this sparsity well. Event-driven graph neural networks (GNNs) are a promising sparse-native alternative, but their irregular structure had, until this paper, no efficient hardware accelerator. EvGNN is presented as the first event-driven GNN accelerator for low-footprint, ultra-low-latency, high-accuracy edge vision, deployed on a Xilinx KV260 Ultrascale+ MPSoC and benchmarked on the N-CARS car-recognition dataset: 87.8% accuracy at an average 16µs latency per event.

## Research problem

Event cameras' microsecond-scale, sparse output is a poor match for CNN accelerators built around dense, regular compute. Event-driven GNNs exploit the sparsity algorithmically, treating each event as a graph node connected to spatiotemporal neighbors, but the resulting graph structure is irregular — variable node degree, dynamic graph construction, sparse memory access patterns — which conventional accelerator architectures (built for fixed, regular dataflows) handle poorly. No efficient hardware accelerator for event-driven GNNs existed prior to this work.

## Key idea

Three co-designed mechanisms make event-driven GNN inference tractable in real time on constrained hardware: (i) directed dynamic graphs using single-hop nodes with edge-free storage, avoiding the memory overhead of storing explicit edge lists; (ii) event queues that efficiently identify local neighbors within a spatiotemporally decoupled search range, rather than a full spatiotemporal neighbor search; (iii) a layer-parallel processing scheme that lets multi-layer GNNs execute with low latency rather than serially layer-by-layer.

## Technical contribution

The first event-driven GNN hardware accelerator design, validated on FPGA rather than left at the algorithm-only or simulation stage; the edge-free directed dynamic graph representation, reducing memory footprint versus explicit graph storage; the spatiotemporally-decoupled event-queue neighbor search; and the layer-parallel multi-layer processing scheme for low end-to-end latency.

## Experimental methodology

Deployed on a Xilinx KV260 Ultrascale+ MPSoC (FPGA-based SoC platform). Benchmarked on the N-CARS dataset, a standard event-camera car-recognition (binary classification) benchmark. Measured classification accuracy and average per-event latency.

## Results

87.8% classification accuracy on N-CARS, with an average latency of 16µs per event — demonstrating real-time, microsecond-resolution event-based vision at the edge on FPGA hardware.

## Comparison with the state of the art

Presented as the first event-driven GNN accelerator; the paper's later citation trail (the Observatory's own [[2026_Kneip_ETHEREAL]] record, by an overlapping author subset — Kneip and Frenkel appear on both) explicitly builds on and scales past this design, moving from FPGA emulation to measured ASIC silicon and from toy/low resolutions to VGA-class (640x480) high-resolution event vision. EvGNN is therefore this Observatory's anchor for the earlier, FPGA-generation step of the event-driven-GNN-hardware lineage that ETHEREAL later extends to real silicon.

## Strengths

First working hardware implementation (not just algorithm) of event-driven GNN inference; genuine algorithm-hardware co-design (all three mechanisms are purpose-built for the graph's irregular access pattern, not a generic GNN accelerator repurposed for events); real FPGA deployment and measurement rather than simulation-only results; directly enables the later, more ambitious ETHEREAL ASIC design from an overlapping author team.

## Weaknesses

Evaluated on a single dataset/task (N-CARS binary car recognition) — no evidence in the abstract-level material of generalization to more complex, multi-class, or higher-resolution event-vision tasks, which is precisely the gap ETHEREAL was built to close two years later; FPGA-based implementation trails what dedicated ASIC silicon (per ETHEREAL) can achieve in latency and energy.

## Limitations

Constrained to relatively low-resolution, low-complexity event-vision tasks by the FPGA platform and the N-CARS benchmark's scope; the edge-free directed dynamic graph representation and event-queue search range are tuned for this task's spatiotemporal event-density regime and may not transfer without modification to denser or sparser event streams.

## Open questions

How does the layer-parallel processing scheme and edge-free graph representation scale to higher-resolution, denser event streams (directly answered two years later by [[2026_Kneip_ETHEREAL]])? Does the approach generalize to non-vision event streams — a question later also raised independently in the audio domain by [[2026_Jeziorek_EventAudioGNNKWS]]?

## Possible extensions

Scaling to higher-resolution datasets and denser event streams (realized by ETHEREAL); porting the architecture to a dedicated ASIC for lower latency and energy (also realized by ETHEREAL); extending to other sensing modalities, independently realized in the audio domain by [[2026_Jeziorek_EventAudioGNNKWS]].

## Relevance to our research

The foundational, earlier-generation paper in the Observatory's [[Event-Driven_Neuromorphic_Accelerators]] Hardware taxonomy node, establishing the event-driven-GNN hardware paradigm that [[2026_Kneip_ETHEREAL]] later scales to real silicon and [[2026_Jeziorek_EventAudioGNNKWS]] independently extends to audio. Corrects an earlier, unverified "T. Liu et al." attribution in the ETHEREAL record's prior-art discussion — the actual FPGA-generation prior work is this paper, by Yang, Kneip, and Frenkel.

## Possible thesis topics

A systematic comparison of the FPGA-generation (EvGNN) and ASIC-generation (ETHEREAL) design choices for event-driven GNN hardware, quantifying exactly what the move to silicon bought in latency/energy versus what algorithmic changes (spline-iterative convolution) contributed (Master's/PhD).

## Possible collaborations

The TU Delft-centered author team (Kneip, Frenkel) directly, given they also authored [[2026_Kneip_ETHEREAL]] — a natural single point of contact for any lab work on event-driven GNN hardware across both FPGA and ASIC generations.

## Links to related papers

[[2026_Kneip_ETHEREAL]] (the same core author team's later ASIC-generation successor design); [[2026_Jeziorek_EventAudioGNNKWS]] (independent extension of the event-graph-GNN hardware paradigm to audio).
