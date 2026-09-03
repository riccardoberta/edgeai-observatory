# FPGA-Based Accelerators of Deep Learning Networks for Learning and Classification: A Review

**Full citation:** Shawahna, A., Sait, S.M., El-Maleh, A. (2018). FPGA-Based Accelerators of Deep Learning Networks for Learning and Classification: A Review. IEEE Access, 7, 7823-7859. DOI: 10.1109/ACCESS.2018.2890150

**PDF:** [arXiv](https://arxiv.org/abs/1901.00121)

**Linked concepts:** [[FPGA]]

## Abstract summary

A comprehensive review of FPGA-based deep learning accelerator designs for both learning (training) and classification (inference), surveying design techniques and comparing reported performance across the field to identify trends directing future accelerator research.

## Research problem

FPGA-based DNN accelerator designs had proliferated across many independent research groups with different design philosophies (loop tiling, dataflow, precision), with no comprehensive review connecting and comparing them.

## Key idea

Systematically review and compare FPGA-based accelerator designs across the field, covering both the inference-focused work most of this concept's other anchors address and the comparatively rarer training-focused designs.

## Technical contribution

A structured, comprehensive taxonomy and comparison of FPGA DNN accelerator designs, one of the most-cited references in the entire FPGA-for-DNN literature.

## Experimental methodology

Literature review and comparative synthesis across published FPGA accelerator designs.

## Results

Extremely widely cited (700+) comprehensive reference, identifying design trends across the field including the inference/training imbalance later quantified more precisely by this concept's own 2024 Yan et al. survey.

## Comparison with the state of the art

Complements this concept's more recent, narrower-scope survey ([[2024_Yan_FPGASurvey]], 287 papers from leading FPGA conferences specifically) with an earlier, more comprehensive review spanning the field's design-technique landscape rather than only quantifying publication trends.

## Strengths

Extremely widely cited; comprehensive scope (training and inference, multiple design techniques); a natural predecessor/complement to this concept's existing Yan et al. 2024 quantitative survey.

## Weaknesses

Predates the 2020s wave of quantization-focused (FINN-successor) and GNN-targeted FPGA accelerator research this concept's Yan et al. anchor identifies as a growing trend.

## Limitations

Review only, no new empirical results; 2018-era snapshot.

## Open questions

How have the design trends this review identified in 2018 evolved by 2024 (per the concept's own Yan et al. survey), and which specific techniques it reviewed have become dominant versus obsolete?

## Possible extensions

A direct comparison of this 2018 review's identified design trends against the 2024 Yan et al. survey's quantitative findings, characterizing exactly how the field's technique mix shifted over six years.

## Relevance to our research

One of the most-cited comprehensive references in the FPGA-for-DNN literature, complementing this concept's existing narrower, more recent survey with a broader, earlier baseline for trend comparison.

## Possible thesis topics

A structured six-year trend comparison (2018 Shawahna et al. review vs. 2024 Yan et al. survey) characterizing how FPGA DNN accelerator design techniques have shifted.

## Possible collaborations

King Fahd University of Petroleum & Minerals (Sait, El-Maleh group).

## Links to related papers

[[2015_Zhang_FPGAAcceleratorDesign]], [[2024_Yan_FPGASurvey]]
