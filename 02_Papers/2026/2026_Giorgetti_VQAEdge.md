# Practical Visual Question Answering at the Edge

**Full citation:** Giorgetti, G., Bianco, S., Firpo, P., Berta, R., Pau, D. (2026). Practical Visual Question Answering at the Edge. LION20 workshop paper (15 pp., appears as a chapter with running head "Danilo Pau et al."). STMicroelectronics, Agrate Brianza; DISCO, Università di Milano-Bicocca; DITEN, University of Genoa.

**PDF:** [lion20.org](https://www.lion20.org/papers/12.pdf)

**Linked concepts:** [[Generative_EdgeAI]] — founding anchor (alongside [[2026_Abdulkadhim_LEAF]]), created 2026-09-04. Also touches [[Distillation]] (knowledge distillation is the core training method for the VQA student models), [[Vision]] (MobileNet V3 Large backbone, VQAv2 dataset), and [[NPU]] (STM32MP2's embedded NPU is the deployment target and the paper reports a measured NPU/CPU speedup).

**Note on authorship:** co-authored by Riccardo Berta (DITEN, University of Genoa) — this Observatory's own research group.

## Abstract summary

Edge devices require AI models tailored to their resource constraints, and deploying multimodal or generative models at the edge is particularly challenging due to memory and compute demands. This paper presents a practical tutorial methodology for developing lightweight multimodal Visual Question Answering (VQA) models for the STM32MP2 low-power MPU platform, covering architectural design and training strategy end to end, plus a proof-of-concept end-to-end generative system that chains the VQA model with speech-to-text, a small language model, and text-to-speech to enable spoken visual question answering. Code, trained models, and instructions are released on GitHub, explicitly aimed at students and newcomers to "Generative EdgeAI" (Gen EdgeAI).

## Research problem

Generative and multimodal models are increasingly of interest for edge deployment (the paper frames this interest as driven by natural, conversational human-machine interaction use cases such as humanoid robotics), but there is very little established practice within the EdgeAI community for designing and integrating such models into end-to-end, application-specific systems — in contrast to the mature literature and model zoos available for traditional fixed/TinyML workloads (CNNs, RNNs). The paper explicitly frames this practical-guidance gap, not a new state-of-the-art architecture, as its motivation.

## Key idea

Rather than pushing VQA accuracy, treat VQA as a tractable "intermediate" multimodal workload — simpler than full open-ended generative chat, more complex than single-modality classification — and use it as a vehicle for a reproducible, code-released tutorial on the full edge-AI workflow (architecture adaptation, knowledge distillation, NPU-aware deployment) that can then be extended toward genuinely generative, conversational Gen EdgeAI systems. The proof-of-concept pipeline (STT → VQA → LM → TTS) demonstrates that extension concretely, even though it is explicitly not tuned or evaluated for end-to-end accuracy.

## Technical contribution

Three lightweight VQA architectures (MFB Baseline, MFB+Attention, MFB+Co-Attention, after Yu et al.) re-engineered for STM32MP2 NPU deployment: ResNet-152 replaced with MobileNet V3 Large, LSTM question encoding replaced with stacked temporal convolutional layers (TCLs), and a simplified MFB fusion module (power normalization removed, sum pooling replaced with average pooling). Knowledge distillation (Hinton et al. formulation, T=3, α=0.1) from a BEiT-3 teacher (683M params, 82.53% VQAv2 test-dev accuracy) to the ~24–51M-parameter student models. A full proof-of-concept generative pipeline integrating the best VQA variant with Moonshine (STT), Gemma 3 270M (LM), and Piper (TTS), with measured per-component latency, power, and memory footprint on real STM32MP2 hardware — not simulated.

## Experimental methodology

VQA models trained and evaluated on VQAv2 (443,757 training / 214,354 validation questions; answer space reduced to the 1,000 most frequent answers, ~87.5% of training data retained). Training on a single NVIDIA GTX 1060 (6GB), Adam, lr=1e-4, 10 epochs (~10h per model). Standard VQA accuracy metric (min(human-annotator-agreement/3, 1), averaged). Deployment measurements taken directly on STM32MP2: CPU vs. NPU inference time for the VQA model; runtime (RTF for streaming STT/TTS, inference time for VQA, tokens/s for the LM), power (W), and memory footprint (Flash/RAM, MB) for all four pipeline components.

## Results

Best VQA variant (MFB+Attention, 40.4M params) reached 57.0% overall VQAv2 validation accuracy (76.7–92.1% depending on answer-frequency band), against 65.4% for the original unmodified 68M-parameter MFB baseline and 82.53%/87.5% for the 683M-parameter BEiT-3 teacher — a substantial but expected accuracy gap traded for a >10x parameter reduction and edge deployability. On-device: the VQA model runs in 434ms on STM32MP2 CPU vs. 56ms on its NPU (7.8x speedup), 0.75W, 48MB Flash, 51MB RAM. Moonshine STT: RTF 1.50, 0.89W, 245MB Flash, 1101MB RAM (CPU only, no NPU support at time of writing). Gemma 3 270M: 4.07 tokens/s (CPU/ollama), 1.00W, 292MB Flash, 789MB RAM. Piper TTS: RTF 1.84, 0.81W, 61MB Flash, 356MB RAM.

## Comparison with the state of the art

Explicitly not targeting SOTA VQA accuracy — positioned against prior edge-VQA systems (MobiVQA on Jetson TX2/Pixel 3XL, the Bilaterally Slimmable Transformer framework, a quantized Transformer VQA model on Samsung Galaxy S23, and TinyVQA on GAP8) as a tutorial-first contribution: unlike those prior device-specific optimization papers, this work releases full training/deployment code and targets a specific, newer MPU class (STM32MP2) with an integrated NPU, rather than reporting only device-specific optimization results.

## Strengths

A genuinely reproducible artifact (code, trained models, and step-by-step instructions on GitHub) rather than only a results paper — directly actionable for thesis/teaching use. Real, non-simulated on-device measurements across latency, power, and memory for all four pipeline stages, not just the novel VQA component. Honest framing throughout: explicitly states the pipeline is not accuracy-tuned end to end and that the goal is feasibility demonstration, not SOTA. Directly co-authored within this Observatory's own research group (Riccardo Berta, DITEN, Genoa), making the released code and models a low-friction extension point for future thesis work.

## Weaknesses

The end-to-end generative pipeline is explicitly not evaluated for accuracy — only per-component latency/power/memory are reported, so the practical usability of the full spoken-VQA interaction loop (e.g., end-to-end response quality, latency, or user-perceived responsiveness) is not established. Gemma 3 270M throughput (4.07 tokens/s) is very slow for a conversational use case; the paper acknowledges this but does not quantify how alternative small LMs (Phi-3/4, Qwen 0.5B/0.6B, Llama 3.2, Granite 3.3 — mentioned only as throughput ranges of 0.4–2.4 tokens/s) would change the user experience. Only the VQA component uses the STM32MP2 NPU; STT, LM, and TTS all run on CPU "due to lack of acceleration at the time of writing" — meaning the reported power/latency figures for 3 of 4 pipeline stages do not reflect what NPU-accelerated versions would achieve, an important caveat for anyone using these numbers as a deployment baseline.

## Limitations

Single-hardware evaluation (STM32MP2 only); no comparison against other Gen-EdgeAI-capable MPU/NPU platforms. The VQA accuracy figures (56–57%) are well below both the original MFB baseline and the teacher model, and the paper does not explore whether more training epochs, additional distillation loss terms, or better hyperparameter tuning could close more of that gap without abandoning deployability. Training used a single consumer GPU (GTX 1060, 6GB) for ~10 hours per model — modest by current standards, but this also means the tutorial's reproducibility bar is genuinely low, which is likely intentional given its pedagogical framing.

## Open questions

What does end-to-end accuracy/quality of the full spoken-VQA pipeline look like once minimally evaluated (rather than left as future work)? How much of the STT/LM/TTS latency and power overhead would NPU acceleration remove once STM32MP2 tooling supports it for those model types? Does the accuracy gap between the lightweight VQA models and the BEiT-3 teacher close further with intermediate-representation distillation (rather than only output-logit distillation, per Hinton et al.) or additional data augmentation?

## Possible extensions

Evaluate the full generative pipeline's end-to-end response quality (not just per-component latency/power/memory) — a natural next step the paper itself leaves open. Benchmark alternative small LMs (Phi-3/4, Qwen 0.5B/0.6B, Llama 3.2, Granite 3.3) for the LM stage under the same STM32MP2 power/latency/memory harness this paper already built, rather than reporting only Gemma 3 270M in depth. Extend NPU acceleration to the STT/LM/TTS stages as STM32MP2 tooling matures, and re-measure the full pipeline's power/latency profile once all four stages are NPU-accelerated.

## Relevance to our research

Directly authored within this group (Riccardo Berta, DITEN); founding anchor, alongside [[2026_Abdulkadhim_LEAF]], of the new [[Generative_EdgeAI]] concept under Applications — the first papers in this Observatory's KB addressing multimodal/generative AI (as opposed to discriminative/classification workloads) deployed specifically on constrained edge hardware. Bridges [[Distillation]] (the training method used), [[Vision]] (VQA's visual backbone and dataset), and [[NPU]] (the deployment target and measured NPU speedup) — and is a natural link into [[MoE_Edge_LLM_Serving]] (Algorithms) since both concern LLMs at the edge, though that cluster focuses on *serving/scheduling* infrastructure for larger dense/MoE LLMs on laptop/workstation-class hardware, while this paper's LM stage (Gemma 3 270M via ollama on an MPU) sits at a genuinely smaller, MCU/MPU-adjacent scale.

## Possible thesis topics

Extending the released VQA/generative pipeline codebase with end-to-end accuracy evaluation and NPU acceleration for the STT/LM/TTS stages, directly building on this group's own released code (Master's-scale, low-friction start given co-authorship access). Benchmarking alternative small LMs and TTS/STT models within the same STM32MP2 power/latency/memory harness this paper established, to build a broader "Gen EdgeAI component zoo" comparable to what exists for discriminative TinyML (Master's/PhD). Investigating whether intermediate-representation (feature-level) distillation, rather than only output-logit distillation, narrows the accuracy gap to the BEiT-3 teacher while preserving NPU-friendliness (Master's).

## Possible collaborations

STMicroelectronics (Gloria Giorgetti, Danilo Pau) — already a direct co-authorship link via this paper; a natural channel for STM32MP2-specific hardware access and continued Gen EdgeAI tutorial work. Università di Milano-Bicocca (Simone Bianco, DISCO) — the paper's other external academic co-author.

## Links to related papers

Founding anchor of [[Generative_EdgeAI]] together with [[2026_Abdulkadhim_LEAF]] (an independently-authored LLM-edge-benchmarking framework, MDPI MAKE 2026) — the two papers approach the same emerging niche from different angles (a practical multimodal tutorial/system here vs. a systematic text-only LLM benchmarking methodology there), which is part of the evidence the niche is real rather than a single group's framing. Cites this Observatory-relevant prior work: Giorgetti & Pau's own 2025 review "Transitioning from TinyML to edge GenAI" (Big Data and Cognitive Computing) — not yet a separate KB record, worth adding if a dedicated survey-level record is wanted. Related-work chain also touches TinyVQA (Rashid et al., GAP8-deployed, KD+quantization) and MobiVQA (Cao et al., Jetson TX2/Pixel 3XL) as prior edge-VQA systems, neither yet recorded in this KB.
