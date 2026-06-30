# HGNAS: Hardware-Aware Graph Neural Architecture Search for Edge Devices

**Full citation:** Zhou, A., Yang, J., Qi, Y., Qiao, T., Shi, Y., Duan, C., Zhao, W., Hu, C. (2024). HGNAS: Hardware-Aware Graph Neural Architecture Search for Edge Devices. IEEE Transactions on Computers, 73(12), 2693-2707. https://arxiv.org/abs/2408.12840

**Linked concepts:** [[NAS]]

## Abstract summary

The authors propose HGNAS, a hardware-aware neural architecture search framework specifically targeting graph neural networks (GNNs) deployed on resource-constrained edge devices, jointly searching the GNN architecture and mapping it to predicted hardware cost (latency, memory, energy) without requiring exhaustive on-device measurement of every candidate.

## Research problem

Most hardware-aware NAS research targets CNNs or simple MLPs; graph neural networks have an irregular computation pattern (variable-size neighborhoods, sparse aggregation) that makes hardware-cost estimation and architecture search substantially harder to adapt from the CNN-centric NAS literature, leaving edge GNN deployment underexplored.

## Key idea

Build a GNN-specific hardware-cost predictor and an efficient search space/strategy tailored to the structural choices unique to GNNs (aggregation type, layer depth, hidden dimensions), enabling hardware-aware search to converge to architectures that are both accurate and efficient on real edge hardware without exhaustively profiling every candidate on-device.

## Technical contribution

A GNN-tailored search space capturing the architectural degrees of freedom specific to graph neural networks; a hardware-cost prediction model for GNN candidate architectures on edge platforms; an efficient search procedure that uses this predictor to jointly optimize accuracy and hardware cost.

## Experimental methodology

Evaluation across multiple graph-learning benchmark datasets and edge hardware platforms, comparing the accuracy/latency/memory trade-off of HGNAS-discovered architectures against hand-designed GNNs and against generic (non-GNN-specific) hardware-aware NAS baselines adapted to graph tasks.

## Results

HGNAS-discovered architectures achieve competitive accuracy with hand-designed GNNs while substantially reducing latency, memory footprint, and/or energy consumption on the target edge hardware, and outperform naively-adapted generic NAS baselines that do not account for GNN-specific structure.

## Comparison with the state of the art

Differentiates itself from the broader hardware-aware NAS literature (which is overwhelmingly CNN-focused, e.g. Once-for-All-style approaches) by explicitly modeling the irregular computation pattern of graph neural networks rather than treating GNN search as a drop-in application of CNN-era NAS techniques.

## Strengths

Addresses a clearly underexplored gap (GNN-specific edge hardware awareness); credible hardware-aware cost modeling tailored to GNN irregularity; published in a peer-reviewed IEEE journal with a detailed evaluation.

## Weaknesses

The graph-learning task domain (e.g. node/graph classification on standard GNN benchmarks) is narrower than the broad vision/audio EdgeAI application space covered elsewhere in this taxonomy, limiting direct transferability of conclusions.

## Limitations

Evaluated primarily on GNN benchmark datasets rather than on EdgeAI-typical sensor/vision/audio workloads; applicability of GNNs themselves to the dominant EdgeAI application categories (Vision, Keyword Spotting, HAR) is itself still a niche, emerging direction.

## Open questions

How well do GNN-specific hardware-cost predictors generalize across very different edge hardware families (Cortex-M vs. NPU vs. FPGA)? Are there emerging EdgeAI sensor applications (e.g. graph-structured sensor networks) where edge GNN deployment becomes broadly relevant?

## Possible extensions

Applying HGNAS-style hardware-aware GNN search to graph-structured sensor-network applications relevant to Industrial IoT or predictive maintenance, where relationships between sensors are naturally graph-structured.

## Relevance to our research

Represents an emerging, niche direction within [[NAS]] research — hardware-aware search extended beyond CNNs to graph neural networks — worth tracking as graph-structured edge applications grow.

## Possible thesis topics

Exploring whether GNN-based models, hardware-aware-searched via HGNAS-style methods, offer advantages over CNN/MLP baselines for graph-structured sensor-network tasks in our Applications taxonomy (e.g. multi-sensor predictive maintenance).

## Possible collaborations

Groups working on graph neural networks for sensor networks and on hardware-cost modeling for irregular computation patterns.

## Links to related papers

[[2017_Zoph_NeuralArchitectureSearchRL]]
