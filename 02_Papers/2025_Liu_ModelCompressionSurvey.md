# A survey of model compression techniques: past, present, and future

**Full citation:** Liu, D., Zhu, Y., Liu, Z., Liu, Y., Han, C., Tian, J., Li, R., Yi, W. (2025). A survey of model compression techniques: past, present, and future. Frontiers in Robotics and AI. DOI: 10.3389/frobt.2025.1518965

**Linked concepts:** [[Compression]]

## Abstract summary

The authors provide a survey of model compression techniques for deep neural networks, organizing the field across the main families of methods (pruning, quantization, knowledge distillation, low-rank factorization, and neural architecture search) and tracing their evolution toward the compression demands posed by very large models, including large language models.

## Research problem

The model compression literature has grown across several largely separate sub-fields (pruning, quantization, distillation, factorization, NAS), developed historically for moderately-sized CNNs/RNNs; the rapid growth of model sizes, especially with LLMs, raises the question of which compression strategies remain effective and which need rethinking, and a unified, up-to-date view across these sub-fields is needed.

## Key idea

Organize and compare model compression methods within a common framework spanning their historical development, current state, and trajectory, paying particular attention to how each family of techniques scales (or fails to scale) to very large modern models.

## Technical contribution

A structured taxonomy and comparative synthesis of pruning, quantization, distillation, low-rank factorization, and NAS-based compression methods; identification of open challenges specific to applying these techniques at LLM scale.

## Experimental methodology

As a survey, the paper does not run new experiments but systematically reviews and compares reported results and methodological characteristics across the compression literature, organized by technique family and by target model scale.

## Results

The survey documents that while each compression family (pruning, quantization, distillation, factorization, NAS) has mature foundations from the CNN era, applying them effectively to very large transformer-based models surfaces new challenges (e.g. calibration cost, structured-vs-unstructured trade-offs, training instability) that are active areas of ongoing research as of 2025.

## Comparison with the state of the art

Complements earlier, narrower compression surveys by explicitly bridging the classic CNN-era compression literature with the LLM-era compression literature, providing an updated reference point for where the field stands after the 2023-2024 wave of LLM-focused compression work (e.g. AWQ, SliceGPT, MiniLLM).

## Strengths

Broad, up-to-date coverage spanning multiple compression sub-fields; useful as an entry point for understanding how classic techniques have been adapted to large models; peer-reviewed.

## Weaknesses

As a survey, it does not provide new empirical evidence; breadth across five technique families necessarily limits depth on any single one compared to dedicated surveys of, e.g., quantization alone.

## Limitations

Coverage of EdgeAI-specific deployment constraints (e.g. microcontroller-class memory budgets) is secondary to the paper's primary focus on general model compression and LLM-scale considerations.

## Open questions

Which compression family scales most gracefully to the largest current models, and does that ranking change for edge-deployment-oriented compression (where memory and energy, not just parameter count, are the binding constraint)?

## Possible extensions

A focused follow-up survey specifically on EdgeAI/microcontroller-oriented compression, cross-referencing this survey's general taxonomy against the hardware constraints specific to our Hardware taxonomy (Cortex-M, RISC-V, NPU).

## Relevance to our research

Useful as a current, citable reference point for the overall state of [[Compression]] research when writing surveys or thesis-proposal background sections.

## Possible thesis topics

A systematic comparison of compression-technique effectiveness specifically under microcontroller-class memory/energy budgets, structured using this survey's taxonomy as a starting framework.

## Possible collaborations

Groups maintaining broad compression benchmarking efforts and survey literature.

## Links to related papers

[[2013_Denil_PredictingParametersDeepLearning]], [[2024_Lin_AWQ]], [[2024_Ashkboos_SliceGPT]], [[2024_Gu_MiniLLM]]
