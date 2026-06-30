# EdgeMark: An Automation and Benchmarking System for Embedded Artificial Intelligence Tools

**Full citation:** Hasanpour, M.A., Kirkegaard, M., Fafoutis, X. (2025). EdgeMark: An automation and benchmarking system for embedded artificial intelligence tools. Journal of Systems Architecture. https://arxiv.org/abs/2502.01700

**Linked concepts:** [[TensorFlow_Lite_Micro]]

## Abstract summary

The authors (Technical University of Denmark) present EdgeMark, an open-source automation system that standardizes and streamlines the workflow of generating, optimizing, converting, and deploying ML models across multiple embedded AI (eAI) tools, and use it to run a comparative benchmark of several widely-used eAI tools including TensorFlow Lite Micro, Edge Impulse, Ekkono, and Renesas eAI Translator.

## Research problem

Comparing different embedded AI deployment tools (TFLM, Edge Impulse, vendor-specific toolchains) is difficult in practice because each has its own model conversion, optimization, and deployment workflow, making fair, reproducible, apples-to-apples benchmarking labor-intensive and rarely done systematically across the whole landscape of available eAI tools.

## Key idea

Build a single automation framework that wraps the model generation, optimization, conversion, and deployment steps of multiple eAI tools behind a common interface, so that the same model and task can be pushed through each tool's pipeline with minimal manual effort, enabling systematic, reproducible cross-tool benchmarking.

## Technical contribution

The EdgeMark automation system itself, designed for modularity, reproducibility, and scalability across eAI tools; an empirical cross-tool benchmark comparing deployment outcomes (accuracy, latency, memory footprint) for TFLM, Edge Impulse, Ekkono, and Renesas eAI Translator on common embedded hardware.

## Experimental methodology

Deployment of common benchmark models through each supported eAI tool's pipeline via the EdgeMark automation layer, measuring resulting inference accuracy, latency, and memory usage on real embedded hardware, and comparing the relative strengths/weaknesses of each tool's optimization pipeline.

## Results

The benchmark surfaces meaningful differences in resource efficiency and ease-of-use across TFLM, Edge Impulse, Ekkono, and Renesas eAI Translator depending on the task and target hardware, demonstrating that no single eAI tool dominates uniformly and that tool choice is a genuine, measurable engineering decision.

## Comparison with the state of the art

Prior comparisons between TFLM and other eAI tools were typically informal or vendor-marketing-driven; EdgeMark provides a reproducible, automation-backed methodology for an apples-to-apples comparison, filling a methodological gap in the embedded AI tooling literature.

## Strengths

Open-source and reproducible; addresses a genuine practical need (informed tool selection) for EdgeAI practitioners; published in a peer-reviewed journal.

## Weaknesses

Benchmark coverage is limited to the specific tools and hardware targets tested; conclusions may not generalize to eAI tools or hardware platforms outside the tested set (e.g. CMSIS-NN-based custom pipelines, or microTVM).

## Limitations

Does not include microTVM, MLIR-based, or ONNX Runtime pipelines in its comparison set, limiting its coverage of the broader Frameworks taxonomy.

## Open questions

How would CMSIS-NN-based custom pipelines and microTVM compare against the tested tools under the same EdgeMark automation methodology? Does tool ranking change significantly across different hardware families (Cortex-M vs. RISC-V vs. DSP)?

## Possible extensions

Extending EdgeMark's automation layer to cover microTVM, MLIR-based toolchains, and ONNX Runtime, to provide a genuinely comprehensive cross-framework benchmark across the whole Frameworks taxonomy.

## Relevance to our research

A useful, reproducible benchmarking methodology directly relevant to [[TensorFlow_Lite_Micro]] tool-selection decisions and to any future Observatory effort to systematically compare frameworks across our taxonomy.

## Possible thesis topics

Extending the EdgeMark benchmark methodology to cover microTVM and CMSIS-NN-based pipelines, producing a more complete cross-framework comparison for a fixed EdgeAI application.

## Possible collaborations

Groups maintaining embedded AI benchmarking infrastructure and tool interoperability standards.

## Links to related papers

[[2021_David_TensorFlowLiteMicro]], [[2024_Carnelos_MicroFlow]]
