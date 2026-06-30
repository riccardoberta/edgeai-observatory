# A survey on FPGA-based accelerator for ML models

**Full citation:** Yan, F., Koch, A., Sinnen, O. (2024). A survey on FPGA-based accelerator for ML models. arXiv:2412.15666. https://arxiv.org/abs/2412.15666

**Linked concepts:** [[FPGA]]

## Abstract summary

The authors survey FPGA-based machine-learning hardware acceleration research, reviewing 287 of 1138 papers published over the past six years across four leading FPGA conferences, finding that inference acceleration dominates over training (81% vs. 13%) and that CNNs remain the dominant target model class, though emerging model types such as GNNs show clear growth.

## Research problem

The FPGA-based ML accelerator literature has grown large and fragmented across venues and model classes; no recent, systematic, quantitative survey existed to map which research directions (inference vs. training, model classes, design techniques) actually dominate current work versus which remain comparatively underexplored.

## Key idea

Apply a systematic, quantitative literature-survey methodology — screening papers from the field's leading FPGA conferences over a six-year window and classifying them along consistent axes (task type, model class, design technique) — rather than a narrative, non-systematic review.

## Technical contribution

A quantitative breakdown of FPGA-based ML accelerator research distribution across inference/training, model class (CNN-dominant but with growing GNN representation), and accelerator design techniques, providing a structured, evidence-based map of the field's current center of mass.

## Experimental methodology

Systematic screening and classification of 287 papers selected from 1138 candidates across four top FPGA conferences over six years, tabulating research focus along the task-type and model-class axes described above.

## Results

Inference acceleration represents 81% of surveyed work versus 13% for training; CNNs remain the dominant target architecture, but GNN-targeted accelerator research shows a clear upward trend, indicating where the field's attention is shifting.

## Comparison with the state of the art

Provides an up-to-date, quantitative complement to earlier, more narrative FPGA-accelerator surveys, and is the first in this taxonomy to explicitly quantify the inference/training imbalance and the CNN-to-GNN shift in FPGA accelerator research focus.

## Strengths

Systematic, quantitative methodology rather than narrative impression; explicitly surfaces an underexplored direction (training acceleration, non-CNN model classes) that a narrative survey might gloss over.

## Weaknesses

Restricted to four FPGA-specific conferences, potentially under-representing FPGA accelerator work published in broader ML-systems or hardware-architecture venues.

## Limitations

A survey by construction does not introduce new accelerator designs; its value is in mapping the field's distribution of effort rather than advancing the state of the art directly.

## Open questions

What explains the persistent 81/13 inference/training imbalance in FPGA accelerator research — is it because training acceleration is technically harder, or because the practical demand is lower? Will GNN-targeted accelerator growth continue as GNN-relevant EdgeAI applications (e.g. graph-structured sensor networks) mature?

## Possible extensions

A follow-up survey specifically tracking training-acceleration and transformer/GNN-targeted FPGA accelerator growth over the next several years; cross-referencing this survey's classification against the [[microTVM_TVM]]/[[MLIR]] compiler-based FPGA deployment literature to see how much of FPGA ML acceleration work now goes through general compilers versus hand-designed accelerators.

## Relevance to our research

Gives the FPGA entry a current, quantitative view of where the field's research effort actually concentrates, useful for prioritizing which FPGA accelerator sub-directions (e.g. GNN-targeted designs) are genuinely emerging versus already saturated.

## Possible thesis topics

A targeted study of FPGA-based training acceleration (the underexplored 13% slice) for a representative EdgeAI model; investigating whether GNN-targeted FPGA accelerator techniques transfer to graph-structured EdgeAI sensing applications.

## Possible collaborations

Groups maintaining FPGA-conference paper corpora or systematic-review tooling that could extend this survey's classification to additional venues or future years.

## Links to related papers

[[2017_Umuroglu_FINN]], [[2023_Zhan_FPGABinaryNN]]
