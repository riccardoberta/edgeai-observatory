# MIMII Dataset: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection

**Full citation:** Purohit, H., Tanabe, R., Ichige, K., Endo, T., Nikaido, Y., Suefusa, K., Kawaguchi, Y. (2019). MIMII Dataset: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection. *Proceedings of the 4th Workshop on Detection and Classification of Acoustic Scenes and Events (DCASE 2019)*. https://dcase.community/workshop2019/ ; dataset: https://zenodo.org/records/3384388

**Linked concepts:** [[Industrial_IoT]]

## Abstract summary

The authors release MIMII, a public dataset of normal and anomalous operating sounds recorded from real industrial machines (valves, pumps, fans, and slide rails) under realistic factory background noise conditions, intended as a shared benchmark for unsupervised acoustic anomaly detection in industrial settings.

## Research problem

Research on sound-based industrial anomaly detection had previously relied on private, non-comparable recordings collected by individual research groups, making it impossible to fairly compare different anomaly-detection methods, and unsupervised methods in particular need realistic normal/anomalous sound examples recorded under real factory noise conditions rather than clean laboratory audio.

## Key idea

Provide a public, realistically noisy dataset of normal and anomalous sounds from several types of real industrial machines, recorded with multiple microphones and at multiple signal-to-noise ratios, so that unsupervised anomaly-detection methods (which typically train only on normal-condition sounds) can be developed and benchmarked under conditions resembling real factory deployment.

## Technical contribution

The dataset itself: recordings from multiple machine types and individual machine units, under several controlled background-noise conditions and signal-to-noise ratios, together with a defined evaluation protocol (training only on normal sounds, evaluating detection of anomalous sounds) suited to the unsupervised anomaly-detection setting that is standard practice in this application area.

## Experimental methodology

Describes the recording setup (machine types, microphone array, background noise mixing at controlled SNR levels) and provides baseline unsupervised anomaly-detection results (e.g. autoencoder-based methods) on the dataset to establish reference performance levels for future comparison.

## Results

Establishes baseline unsupervised anomaly-detection performance across the different machine types and noise conditions, demonstrating that detection difficulty varies meaningfully with machine type and background noise level — a realistic complexity that prior, cleaner private datasets did not capture.

## Comparison with the state of the art

Fills a clear gap relative to prior industrial-sound anomaly-detection research, which lacked any shared, public, realistically noisy benchmark; MIMII became a standard reference dataset (and inspired follow-on DCASE challenge editions) for the subfield.

## Strengths

Public and freely available, covering multiple machine types and realistic background noise/SNR conditions, with a standard evaluation protocol that enables direct comparison across different anomaly-detection methods and papers.

## Weaknesses

Covers a limited, specific set of machine types (valves, pumps, fans, slide rails) and recording conditions, which may not represent the full diversity of real industrial acoustic environments and machinery encountered in deployment.

## Limitations

As a dataset rather than a method, its value depends on continued community adoption; it does not itself address how a trained anomaly detector should be deployed and run efficiently on resource-constrained edge/IoT hardware in the field.

## Open questions

How well do anomaly-detection methods trained and validated on MIMII generalize to machine types and noise conditions not represented in the dataset? What additional dataset coverage (machine types, fault types, recording conditions) is most needed to support real industrial deployment research?

## Possible extensions

Extending the dataset's machine-type and fault-type coverage; pairing the dataset with standardized on-device (edge/microcontroller) deployment benchmarks, so anomaly-detection accuracy and on-device resource cost can be reported together.

## Relevance to our research

The key enabler dataset for the acoustic-based industrial anomaly-detection research direction tracked in the [[Industrial_IoT]] knowledge-base entry; the standard benchmark against which any new unsupervised industrial sound anomaly-detection method should be evaluated.

## Possible thesis topics

Benchmarking a Tiny-MLOps-style on-device unsupervised anomaly detector directly on MIMII recordings under realistic SNR conditions, to connect its previously reported microcontroller-deployment results to this standard public benchmark.

## Possible collaborations

The DCASE challenge community and groups working on acoustic industrial anomaly detection and dataset extension.

## Links to related papers

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]]
