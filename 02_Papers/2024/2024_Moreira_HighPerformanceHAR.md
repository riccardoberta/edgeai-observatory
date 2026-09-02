# High-Performance Real-Time Human Activity Recognition Using Machine Learning

**Full citation:** Moreira, F. (2024). High-Performance Real-Time Human Activity Recognition Using Machine Learning. Mathematics, 12(22), 3622. DOI: 10.3390/math12223622

**PDF:** [MDPI (open access)](https://www.mdpi.com/2227-7390/12/22/3622)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Human_Activity_Recognition]]

## Abstract summary

Presents a real-time HAR system deployed on the STMicroelectronics B-L475E-IOT01A Discovery Kit (a low-power Cortex-M microcontroller platform) using integrated accelerometer/gyroscope sensors. The model classifies dynamic activities (walking, walking upstairs, walking downstairs) with high precision and recall, but shows lower recall for distinguishing static activities (sitting vs. standing) due to subtle postural signal differences. Advanced feature extraction, data augmentation, and sensor fusion techniques are used to improve accuracy, reaching 90% overall classification accuracy, validated in real time via a Tera Term interface.

## Research problem

Wearable/embedded HAR systems must classify activities in real time on low-power microcontroller hardware, but dynamic activities (walking variants) and static activities (sitting/standing) present different recognition challenges — static activities in particular are hard to distinguish from accelerometer/gyroscope signals alone due to subtle postural differences, a gap not always addressed explicitly in HAR deployment studies.

## Key idea

Deploy a machine-learning HAR pipeline directly on a real, off-the-shelf low-power microcontroller development kit (B-L475E-IOT01A) with real-time validation, and explicitly characterize where the resulting system succeeds (dynamic activities) and struggles (static activity discrimination), using feature extraction, data augmentation, and sensor fusion to close part of that gap.

## Technical contribution

A validated, real-time, on-device HAR deployment on genuine low-power Cortex-M-class hardware (not just an offline model benchmark), with an explicit, honest characterization of the dynamic-versus-static activity recognition gap and the specific techniques (advanced feature extraction, data augmentation, sensor fusion) used to narrow it.

## Experimental methodology

Model development and deployment on the B-L475E-IOT01A Discovery Kit using onboard accelerometer/gyroscope sensors; real-time activity classification validated through a Tera Term serial interface; evaluated for precision/recall across dynamic (walking, walking upstairs, walking downstairs) and static (sitting, standing) activity classes.

## Results

90% overall classification accuracy with high precision/recall for dynamic activities; lower recall specifically for static activity discrimination (sitting vs. standing) attributed to subtle postural signal differences, an honestly reported limitation rather than an omitted one.

## Comparison with the state of the art

Complements the architecture-focused HAR literature already in this Observatory's [[Human_Activity_Recognition]] concept (DeepConvLSTM, [[2024_Lattanzi_TransformersTinyHAR]]'s tiny-transformer feasibility study) with a genuine real-time, real-hardware deployment validation on a specific, reproducible low-power development kit, directly answering that concept's own open problem about deployment-realistic (not just offline) evaluation.

## Strengths

Real, reproducible hardware target (a standard commercial development kit, not a custom board); honest reporting of a specific failure mode (static-activity recall) rather than only headline accuracy; fully open-access, full-text-verifiable.

## Weaknesses

Single hardware platform and sensor configuration; the static-activity recognition gap, while honestly reported, is not fully resolved by the paper's own techniques.

## Limitations

Accelerometer/gyroscope-only sensing may be fundamentally limited for static posture discrimination regardless of algorithmic improvements, suggesting the gap may require additional sensing modalities (e.g. pressure, EMG) rather than purely algorithmic fixes.

## Open questions

Would additional sensing modalities (beyond accelerometer/gyroscope) close the static-activity recognition gap this paper identifies, or is further algorithmic/feature-engineering work sufficient? How does this system's real-time, real-hardware accuracy compare directly to the offline benchmark numbers reported for the architecture families already in this Observatory's [[Human_Activity_Recognition]] concept?

## Possible extensions

Testing whether additional low-power sensing modalities (e.g. barometric pressure for elevation change, or a lightweight EMG channel) close the static-activity discrimination gap this paper identifies and partially addresses via feature engineering alone.

## Relevance to our research

Directly answers this Observatory's own [[Human_Activity_Recognition]] open problem — "how do the most accurate wearable HAR architectures perform when actually deployed on Cortex-M-class hardware under realistic power budgets" — with a real, reproducible, honestly-reported deployment on standard commercial low-power hardware.

## Possible thesis topics

Extending this real-time B-L475E-IOT01A HAR deployment with an additional sensing modality specifically targeting the static-activity discrimination gap it identifies (sitting vs. standing).

## Possible collaborations

Groups working on wearable/embedded HAR deployment on commercial low-power microcontroller platforms.

## Links to related papers

[[2024_Lattanzi_TransformersTinyHAR]]
