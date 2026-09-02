# Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis

**Full citation:** Paula, T. S., Kupssinskü, L. S., Barros, R. C. (2026). Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis. arXiv:2606.27634 [cs.LG]. MALTA (Machine Learning Theory and Applications Lab), PUCRS, Porto Alegre, Brazil; Kunumi Institute, Brazil. Submitted 26 Jun 2026. License CC BY 4.0. DOI: 10.48550/arXiv.2606.27634.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2606.27634)

**Linked concepts:** [[Continual Learning]], [[On-device Learning]]

**Verification note:** the full-text HTML fetch for this paper was truncated by the fetch tool partway through Section 5 (Main Results), before reaching the specific correlation statistics and per-model KL-divergence figures. The abstract, introduction, and full methodology (Sections 1–4, including the TRACE task selection and stability-metric definitions) were independently verified from the full text. The specific numbers below attributed to the 2026-07-05 weekly digest (Pearson r, the KL "failure zone," and per-model KL peaks) were reported by that digest's own full-text read and are carried forward here as digest-sourced rather than independently re-verified in this pass — re-check before citing in a survey or thesis.

## Abstract summary

Small Language Models (SLMs) are increasingly considered for edge deployment (laptops), enabling private, low-latency, locally personalized applications — but personalization requires continual adaptation to evolving user/task data, risking catastrophic forgetting. The paper studies sequential LoRA personalization of SLMs, saving checkpoints after each adaptation stage and evaluating them on current, previously-seen, and a fixed reference task set. This checkpoint-level protocol enables monitoring of task performance, forgetting, and reference-set drift over time. Lightweight reference-set distributional diagnostics are shown to reveal model-specific instability patterns during sequential LoRA personalization, including cases where task-level metrics alone hide harmful adaptation.

## Research problem

Deploying SLMs (≤1B params) on-device for private, personalized applications puts them in a continual-learning setting: personalization must adapt to evolving user/task data over time. Recent benchmarks (TRACE) show continual fine-tuning can significantly degrade the general abilities of aligned LLMs, but task-level accuracy metrics alone may not reveal this degradation as it happens — a model can look fine on its target tasks while quietly drifting in ways that harm its broader capabilities.

## Key idea

Monitor model checkpoints after each sequential adaptation stage not just on task accuracy, but on lightweight distributional diagnostics — KL divergence, entropy, and margin — computed against a fixed reference set and the base (pre-adaptation) model. The hypothesis is that these cheap, model-agnostic diagnostics can reveal instability that task-level continual-learning metrics (accuracy, backward/forward transfer) miss.

## Technical contribution

A checkpoint-level stability-monitoring protocol inspired by TRACE's evaluation logic but focused on a smaller task set and on stability rather than only task performance; three specific lightweight diagnostics (KL divergence from the base model's next-token distribution, entropy of next-token probabilities, and margin between top-two predictions); an empirical analysis across three SLM families (Qwen 3.5 0.8B, Llama 3.2 1B Instruct, Gemma 3 1B IT) and three TRACE tasks (FOMC — hawkish/dovish finance classification; ScienceQA; NumGLUE-CM — arithmetic reasoning), identifying an order-invariant internal stability signature per model family.

## Experimental methodology

Sequential LoRA fine-tuning of three SLMs (Qwen 3.5 0.8B, Llama 3.2 1B Instruct, Gemma 3 1B IT) across three TRACE-derived tasks (FOMC, ScienceQA, NumGLUE-CM, each with a 500-example evaluation subset, drawn from TRACE's original repository), with no replay. After each adaptation stage, a checkpoint is saved and evaluated on the current task, all previously seen tasks, and the fixed reference set, building a checkpoint-by-task accuracy matrix plus the three stability diagnostics. Standard continual-learning metrics computed: Learning Accuracy (diagonal-entry performance immediately after learning each task), Backward Transfer, Forward Transfer, and the immediate adaptation gain Δ_adapt per task.

## Results

All three models achieve their largest immediate adaptation gain after training on FOMC, suggesting this is a broadly useful first adaptation step regardless of architecture. NumGLUE-CM is identified as the most harmful task by Δ_adapt (the file read in this pass was truncated before the exact figure). Per the 2026-07-05 weekly digest's own full-text read (not independently re-verified here): reference-set KL divergence from the base model tracks performance collapse with Pearson r ≈ −0.5 (p < 0.001), is order-invariant (the same trajectory occurs when task order is reversed), and shows an apparent "failure zone" around KL ≈ 0.8; Gemma showed high instability (KL to base peaking around 1.62, with sharp backward-transfer degradation), while Qwen stayed comparatively anchored (KL around 0.30, with even positive backward transfer).

## Comparison with the state of the art

Explicitly builds on and extends TRACE's evaluation methodology (Overall Performance and Backward Transfer metrics, plus broader ability/instruction-following/safety deltas) by adding checkpoint-level distributional stability diagnostics that TRACE itself does not include. Not benchmarked against other continual-learning algorithms — the contribution is diagnostic/monitoring, not a new adaptation method, so there is no accuracy-improvement claim to compare against prior CL techniques.

## Strengths

A genuinely novel framing: treating on-device SLM personalization as a stability-monitoring problem rather than only a forgetting-mitigation problem; the diagnostics (KL divergence, entropy, margin) are cheap enough to plausibly run on-device as an early-warning signal, which matters directly for real deployment, not just offline analysis; the order-invariance property (if it holds, per the digest's reading) is a strong and checkable claim — a genuinely useful diagnostic should not depend on which order tasks happen to arrive in; testing across three different SLM families surfaces a real, interesting result (distinct "intrinsic stability fingerprints" per model family) rather than reporting a single model's behavior.

## Weaknesses

Experiments run on a Titan X GPU with full-precision LoRA fine-tuning — not validated under quantization or on constrained/embedded hardware, which is exactly the deployment regime this Observatory's lab operates in; only three TRACE tasks and three model families are tested, a fairly narrow empirical base for claims about a general "stability fingerprint" phenomenon; the paper is explicit that this is a diagnostic study, not a new CL algorithm, so it does not itself solve the forgetting problem it characterizes.

## Limitations

The correlation and failure-zone figures reported by the 2026-07-05 digest (Pearson r ≈ −0.5, KL ≈ 0.8 failure zone) were not independently re-verified in this pass due to a full-text fetch truncation and should be re-confirmed from the PDF before being treated as settled facts in a thesis or survey. The stability diagnostics are validated only in a no-replay, sequential-task setting; how they behave under replay-based continual learning or concurrent multi-task adaptation is untested.

## Open questions

Does the KL-divergence early-warning signal survive quantization (INT8/INT4) — i.e., is it usable as an on-device trigger for continual on-device learning on actual constrained hardware, as the 2026-07-05 digest's suggested thesis hook proposes? Does the order-invariant "stability fingerprint" generalize to more than three SLM families and more than three tasks, or is it an artifact of this specific experimental design? Can the diagnostic be turned into an actionable intervention (e.g., automatically triggering a rollback or a reduced learning rate) rather than only a passive monitoring signal?

## Possible extensions

Test whether the KL-divergence stability signal survives quantization and works as an on-device early-warning trigger for continual on-device learning (the explicit 2026-07-05 digest hook); extend the three-task, three-model empirical base to more SLM families and a wider TRACE task set to test the generality of the "intrinsic stability fingerprint" finding; turn the passive diagnostic into an active intervention (automatic rollback/learning-rate adjustment) and evaluate whether it actually prevents the harmful adaptation it detects.

## Relevance to our research

A strong conceptual fit for the Observatory's [[Continual Learning]] and [[On-device Learning]] branches, and an early (June 2026) data point in what became, per the July 2026 monthly report, a broader on-device-training research arc spanning the rest of the summer (RISC-V float16 training, Hailo-8L accelerator repurposing, ECRAM continual learning). Directly connects the LLM-on-edge trend to the classic forgetting literature already tracked (Kirkpatrick EWC, iCaRL).

## Possible thesis topics

Test whether the KL-divergence stability signal from this paper survives quantization and works as an on-device early-warning trigger for continual on-device learning (Master's/PhD, per the 2026-07-05 digest's suggested hook) — a natural pairing with the Observatory's existing on-device training records. Extend the three-model, three-task empirical base to test whether "intrinsic stability fingerprints" are a general model-family property or an artifact of this specific setup (Master's).

## Possible collaborations

The MALTA Lab (PUCRS, Porto Alegre) and Kunumi Institute, given their direct focus on continual personalization of small/edge-deployable language models.

## Links to related papers

Connects to the existing continual-learning entries [[2017_Kirkpatrick_OvercomingCatastrophicForgetting]] (EWC) and [[2017_Rebuffi_iCaRL]] as the Observatory's first record specifically on continual *personalization* of small/edge language models, extending that older forgetting literature into the on-device-LLM era.
