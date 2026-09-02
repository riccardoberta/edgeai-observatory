# TinyML-Enabled Edge Implementation of Transfer Learning Framework for Domain Generalization in Machine Fault Diagnosis

**Full citation:** Asutkar, S., Chalke, C., Shivgan, K., Tallur, S. (2022). TinyML-enabled edge implementation of transfer learning framework for domain generalization in machine fault diagnosis. *Expert Systems with Applications*, 213, Part B, 119016. DOI: 10.1016/j.eswa.2022.119016

**PDF:** [DOI](https://doi.org/10.1016/j.eswa.2022.119016) · [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417422020346)

**Verification note:** ScienceDirect returns a client-rendered, non-fetchable abstract page; bibliographic details and technical summary confirmed via WebSearch cross-referencing ResearchGate and the ouci.dntb.gov.ua indexing record. This record is abstract-level verified, not full-text-verified. Cited by DOI-registration year (2022); the paper appears in *Expert Systems with Applications* volume 213, Part B, whose print compilation is dated 2023 in some indexes.

**Linked concepts:** [[Predictive_Maintenance]], [[Industrial_IoT]]

## Abstract summary

Proposes a lightweight 1D-CNN-based transfer-learning framework for machine fault diagnosis, explicitly optimized for edge/IoT deployment on devices like Raspberry Pi and ESP32. The framework fine-tunes convolutional layers while transferring dense layers from a source model, and introduces a memory-efficient retraining method that adapts only bias terms, targeting domain generalization (adapting a fault-diagnosis model trained on one machine/condition to a new, related one) under tight edge memory and compute budgets.

## Research problem

Fault-diagnosis models trained on one machine or operating condition (the "source domain") typically degrade when deployed on a different but related machine or condition (the "target domain") without retraining, but full retraining is often infeasible on resource-constrained edge IoT devices used for smart sensor nodes in industrial fault diagnosis — creating a tension between domain generalization (which normally wants more adaptation capacity) and TinyML deployment constraints (which want less).

## Key idea

Use transfer learning with a selective fine-tuning strategy, fine-tune convolutional feature-extraction layers while transferring dense/classification layers directly, and add a memory-efficient retraining mode that adjusts only bias parameters, so that domain adaptation for a new machine/condition can happen on-device with a fraction of the memory and compute a full retrain would require.

## Technical contribution

A 1D-CNN transfer-learning framework specifically designed for edge deployment of fault-diagnosis domain generalization, including a bias-only retraining mode as a memory-efficient on-device adaptation strategy; validated on real edge hardware (Raspberry Pi, ESP32) rather than only in simulation.

## Experimental methodology

1D-CNN fault-diagnosis models trained on a source domain and adapted to target domains via (a) standard fine-tuning of convolutional layers with transferred dense layers and (b) the proposed bias-only retraining method; deployed and evaluated for feasibility on Raspberry Pi and ESP32 edge devices (per the abstract; specific fault-diagnosis dataset and accuracy figures not captured in this record beyond the general framing).

## Results

The transfer-learning framework, and particularly the bias-only retraining variant, demonstrated that domain generalization for machine fault diagnosis is achievable within the memory and compute budgets of TinyML-class edge devices (Raspberry Pi, ESP32), reducing the retraining cost relative to full-model fine-tuning while retaining useful fault-diagnosis accuracy on the target domain (per the published abstract).

## Comparison with the state of the art

Distinguishes itself from cloud-centric or full-retraining transfer-learning approaches to fault diagnosis by explicitly co-designing the adaptation strategy (bias-only retraining) around edge hardware constraints, and from the multi-objective NAS-based approach of [[2023_Ma_LightweightFaultDiagnosisNAS]] by focusing on adapting a fixed architecture across domains rather than searching for a new lightweight architecture per deployment.

## Strengths

Directly targets the practically important domain-shift problem in industrial fault diagnosis (a model trained on one machine rarely transfers perfectly to another); bias-only retraining is a concrete, memory-efficient on-device adaptation technique validated on real TinyML hardware (Raspberry Pi, ESP32), not just simulated.

## Weaknesses

As an abstract-level record (ScienceDirect full text not fetchable), this summary lacks the specific fault-diagnosis dataset, machine types, and quantitative accuracy-retention figures for the bias-only method versus full fine-tuning.

## Limitations

Effectiveness of bias-only retraining likely depends on how similar the source and target domains are; large domain shifts (very different machine types or fault modes) may exceed what bias-only adaptation can compensate for, requiring the heavier fine-tuning fallback.

## Open questions

How large a domain shift can bias-only retraining tolerate before accuracy degrades unacceptably, and is there a principled way to decide on-device whether bias-only adaptation suffices or full fine-tuning is needed? How does this transfer-learning-based approach compare quantitatively, on the same fault-diagnosis task, against the NAS-based lightweight-architecture approach of [[2023_Ma_LightweightFaultDiagnosisNAS]]?

## Possible extensions

A direct empirical comparison of transfer-learning-based domain adaptation (this paper) versus per-domain lightweight architecture search (as in [[2023_Ma_LightweightFaultDiagnosisNAS]]) on the same fault-diagnosis benchmark and edge hardware, to characterize when each strategy is preferable.

## Relevance to our research

A concrete anchor for [[Predictive_Maintenance]] and [[Industrial_IoT]] on the domain-generalization problem specifically, an issue distinct from but complementary to model compression/NAS, and directly relevant whenever the Observatory discusses deploying fault-diagnosis models across heterogeneous industrial equipment fleets.

## Possible thesis topics

Developing and empirically validating criteria for choosing between bias-only retraining and full fine-tuning for on-device domain adaptation in industrial fault diagnosis, potentially combined with continual-learning techniques to handle sequential domain shifts.

## Possible collaborations

Groups working on TinyML deployment for industrial IoT and domain-adaptation/transfer-learning research applied to predictive maintenance.

## Links to related papers

[[2023_Ma_LightweightFaultDiagnosisNAS]]
