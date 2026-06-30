# Embedded Machine Learning for Microcontroller-Class Edge Devices: Data, Feature, Evaluation, and Deployment Pipelines

**Full citation:** Darvishi, M. (2026). Embedded Machine Learning for Microcontroller-Class Edge Devices: Data, Feature, Evaluation, and Deployment Pipelines. arXiv:2606.18122 [cs.LG, cs.AI, cs.AR, eess.AS, eess.SP]. Submitted 16 June 2026. 6 pages, 3 figures, 4 tables. DOI: 10.48550/arXiv.2606.18122.

**Access note:** Full text retrieved via Google's PDF viewer (docs.google.com/viewer) after the arXiv HTML conversion was unavailable for this submission and direct PDF fetches were rate-limited; the rendered text was read directly from the viewer, not transcribed from a screenshot.

**Linked concepts:** [[Human_Activity_Recognition]], [[Biosignals]], [[Cortex-M]]

## Abstract summary

A systems-oriented, tutorial-style synthesis of the embedded machine-learning workflow for microcontroller-class platforms, covering sampling/buffering, feature extraction as dimensionality reduction, validation under class imbalance, model/runtime co-design, and streaming deployment. Two running examples are used throughout: inertial motion recognition (RMS + spectral features from a 2-second, 3-axis accelerometer window) and keyword spotting (MFCC features into a compact 1D CNN).

## Research problem

Generic machine-learning introductions and many embedded-ML demonstrations leave out the engineering decisions that actually determine whether a model can be deployed on a microcontroller: how raw sensor streams become bounded input tensors, how validation should be structured to avoid overstating field performance, and how acquisition, feature extraction, and inference are scheduled without dropping samples. The paper aims to make these decisions explicit rather than treating "deployment" as an afterthought to model training.

## Key idea

Treat embedded ML as a closed-loop systems-engineering pipeline — sensing, preprocessing, feature extraction, training, deployment, and field monitoring (Fig. 1) — rather than as model training followed by export. Two concrete pipelines instantiate this: a windowed inertial pipeline (raw accelerometer samples → RMS/PSD features → small dense classifier, Fig. 2) and a streaming audio pipeline (anti-aliased sampling → sliding-window MFCC → compact 1D CNN → softmax, Fig. 3).

## Technical contribution

Not a new algorithm but a structured reference framework and vocabulary: a closed-form raw-input-size formula N_raw = f_s·T·C for windowed sensor pipelines; a worked dimensionality-reduction example (375 raw accelerometer values per 2-second window reduced to 33 RMS/PSD features, more than an order-of-magnitude reduction); a deployment-oriented evaluation taxonomy (Table II: predictive quality, error analysis, runtime, memory, compute, energy, each tied to why it matters embedded-side); a runtime/deployment-consideration checklist (Table III); a deployment-pattern summary connecting the two case studies to generalizable lessons (Table IV); and eight numbered "practical design rules" for moving from an offline-trained model to a reliable on-device system.

## Experimental methodology

The paper is a synthesis/tutorial, not an empirical study with a held-out test set: it does not report a new trained model evaluated on a new dataset. Its "experiments" are worked numerical examples (e.g., 62.5 Hz sampling over a 3-axis, 2-second window → 375 raw values → 750 bytes as 16-bit integers before double buffering, feature memory, weights, activations, and runtime arena are added) used to illustrate the design rules, plus qualitative case-study walkthroughs of the inertial and audio pipelines.

## Results

No accuracy, latency, or energy numbers are reported for a specific trained model — the "results" are the structured deployment framework itself (Tables I–IV) and the worked memory-budget arithmetic for the two case studies. The inertial example's headline numbers are the 375→33 feature-dimension reduction and the 750-byte raw-buffer estimate; the audio example's are qualitative (MFCC + 1D convolution as a compact, locality-exploiting representation).

## Comparison with the state of the art

The paper does not benchmark against other systems; it positions itself relative to existing tools (Edge Impulse, TensorFlow Lite Micro, CMSIS-NN) as a vehicle-agnostic architectural pattern that any of them can implement, and cites MCUNet, quantization-aware training, pruning, and NAS as the broader state of the art in model-side compression that its systems framework complements rather than competes with.

## Strengths

Clear, reusable formalization of practical but rarely-written-down engineering rules (the N_raw formula, the deployment-metric taxonomy, the eight design rules); explicit treatment of evaluation pitfalls specific to embedded deployment (accuracy being misleading under class imbalance, the need for session/subject-separated validation splits, temporal smoothing for sliding-window classifiers); a useful call for more rigorous scientific reporting in embedded-ML papers (target device, clock frequency, numerical precision, memory, latency, energy, sampling assumptions — explicitly listed); concise and well-organized for teaching or onboarding purposes.

## Weaknesses

No novel empirical contribution — no new model, dataset, or measured result is presented; all numbers are illustrative arithmetic, not measurements on real hardware. The two case studies are described at a conceptual level without reporting actual classifier accuracy, memory footprint, or latency figures, which limits its usefulness as a citable benchmark or baseline. Single-author paper with no apparent peer-reviewed venue at the time of writing (arXiv preprint only).

## Limitations

As a tutorial/synthesis rather than original research, it cannot be used to support claims requiring empirical evidence (e.g., "method X achieves Y% accuracy at Z latency"); its value is pedagogical and organizational rather than as a source of new findings. The open-research-directions section (continual learning, uncertainty calibration/OOD detection, verification of probabilistic components, application-specific acceleration beyond MAC throughput, privacy-preserving field monitoring) is asserted rather than substantiated with new evidence.

## Open questions

The paper itself frames several open problems rather than answering them: how to do continual learning on-device without catastrophic forgetting under tight memory; how to calibrate uncertainty and detect out-of-distribution inputs on constrained hardware; how to verify threshold/rejection logic for probabilistic, data-dependent components at the system level; how to design accelerators for full pipelines (filtering, MFCC, buffering) rather than only matrix multiplication.

## Possible extensions

Pairing this systems framework with an empirical study — e.g., applying the eight design rules to a concrete inertial or audio dataset and measuring whether following them actually improves field robustness versus a naive train/deploy approach; using the deployment-metric taxonomy (Table II) as a standard reporting template when writing up future Observatory paper analyses, to flag papers that omit memory/latency/energy figures.

## Relevance to our research

Useful primarily as a teaching and onboarding reference for the Observatory rather than as a `02_Papers/` empirical source: it gives a vocabulary and checklist (the N_raw formula, the deployment-metric taxonomy, the eight design rules) that can be reused when evaluating reproducibility and completeness of other papers' reporting. Connects to [[Human_Activity_Recognition]] (the inertial RMS/PSD case study) and [[Biosignals]]/sensing pipelines more broadly, and to [[Cortex-M]] as the implicit target hardware class throughout.

## Possible thesis topics

An empirical validation study that takes the paper's eight design rules and measures, on a real inertial or audio dataset and real MCU hardware, how much field robustness or reproducibility actually improves when the rules are followed versus a naive baseline pipeline; a "reporting completeness" survey of recent embedded-ML papers scored against the Table II deployment-metric taxonomy, to quantify how common the under-reporting problem the paper criticizes actually is.

## Possible collaborations

Less suited to a research collaboration than to internal use as a checklist/reference; could inform a joint teaching module if the lab develops EdgeAI coursework, given the paper's explicit avoidance of basic ML notions in favor of deployment-specific engineering content.

## Links to related papers

[[2018_Lai_CMSIS-NN]] (cited deployment-runtime reference, ref. [4]), [[2021_David_TensorFlowLiteMicro]] (cited deployment-runtime reference, ref. [3]), [[2018_Warden_SpeechCommands]] (cited dataset reference, ref. [5]), [[2017_Jacob_QuantizationIntegerOnlyInference]] (cited quantization reference, ref. [8])
