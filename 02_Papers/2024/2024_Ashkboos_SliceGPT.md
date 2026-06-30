# SliceGPT: Compress Large Language Models by Deleting Rows and Columns

**Full citation:** Ashkboos, S., Croci, M.L., Gennari do Nascimento, M., Hoefler, T., Hensman, J. (2024). SliceGPT: Compress Large Language Models by Deleting Rows and Columns. Proceedings of ICLR 2024. https://arxiv.org/abs/2401.15024

**Linked concepts:** [[Pruning]]

## Abstract summary

The authors (Microsoft Research, ETH Zurich) propose SliceGPT, a post-training structured-pruning method that exploits computational invariance in transformer architectures (specifically, invariance under orthogonal transformation of residual-stream representations) to delete entire rows and columns of weight matrices, physically shrinking matrix dimensions rather than just zeroing out individual weights.

## Research problem

Most LLM pruning methods produce unstructured or semi-structured sparsity (zeroed-out individual weights) that requires specialized sparse-matrix hardware/kernels to realize real speedups; dense, structured compression that yields smaller, denser matrices usable on standard hardware is harder to achieve without large accuracy loss.

## Key idea

Because of the way layer normalization and residual connections compose in transformers, the representations passing between layers can be rotated by an orthogonal matrix without changing the network's function (computational invariance); SliceGPT uses principal component analysis on layer activations to choose a rotation that concentrates information into a smaller number of dimensions, then physically slices away the now-low-information rows/columns of the weight matrices.

## Technical contribution

A formal characterization of the computational invariance property in transformer architectures; a PCA-based method for choosing the rotation and slicing point; the resulting smaller, dense weight matrices that work directly with standard dense-matrix-multiplication hardware, unlike unstructured sparsity.

## Experimental methodology

Evaluation on OPT and LLaMA-2 model families at multiple sizes, measuring zero-shot task accuracy and perplexity after removing up to 25% of model parameters (including embeddings), and measuring inference throughput/memory on consumer and single-GPU hardware, compared against other structured-pruning baselines.

## Results

SliceGPT removes up to 25% of parameters in large OPT/LLaMA-2 models while retaining 99% (OPT) or 95% (LLaMA-2) of zero-shot task performance, and delivers actual measured speedups on consumer GPUs and a single high-end GPU because the resulting matrices stay dense.

## Comparison with the state of the art

Unlike unstructured/semi-structured pruning methods that need specialized sparse kernels to realize speedups in practice, SliceGPT's structured slicing produces smaller dense matrices that run faster on standard hardware out of the box, making it more directly deployable.

## Strengths

Theoretically grounded (formal invariance argument, not just empirical heuristic); produces real, hardware-realizable speedups without specialized kernels; works post-training without full retraining.

## Weaknesses

Accuracy retention is lower for LLaMA-2 than OPT, suggesting the invariance-exploiting approach is somewhat architecture/training-dependent; larger compression ratios (beyond ~25%) show more significant degradation.

## Limitations

Demonstrated on GPU-class hardware; transferability of the slicing approach to microcontroller-class or highly resource-constrained edge targets is not evaluated.

## Open questions

How does SliceGPT-style structured slicing interact with quantization (combined compression)? Does the computational-invariance argument extend to other normalization schemes beyond the ones studied?

## Possible extensions

Combining SliceGPT's structured slicing with activation-aware quantization ([[2024_Lin_AWQ]]) for compounded compression; extending the invariance argument to smaller, edge-deployable transformer variants.

## Relevance to our research

A theoretically grounded alternative to classic magnitude-based pruning, relevant to the 2023-2024 shift in [[Pruning]] research toward structured compression of large transformer models for efficient deployment.

## Possible thesis topics

Evaluating whether SliceGPT-style structured slicing of small/edge transformer models retains accuracy at compression ratios needed for microcontroller-class deployment, compared against classic magnitude pruning.

## Possible collaborations

Groups working on transformer compression theory and on dense-matrix-optimized inference kernels for edge GPUs/NPUs.

## Links to related papers

[[1990_LeCun_OptimalBrainDamage]], [[2015_Han_LearningWeightsConnections]]
