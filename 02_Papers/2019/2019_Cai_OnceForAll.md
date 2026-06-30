# Once-for-All: Train One Network and Specialize it for Efficient Deployment

**Full citation:** Cai, H., Gan, C., Wang, T., Zhang, Z., Han, S. (2019). Once-for-All: Train One Network and Specialize it for Efficient Deployment. arXiv:1908.09791. https://arxiv.org/abs/1908.09791

**Linked concepts:** [[NAS]]

## Abstract summary

The authors propose training a single "once-for-all" (OFA) network that contains within it many sub-networks, from which the sub-network best suited to a given hardware device and a given latency/energy constraint can be extracted directly, without further training.

## Research problem

Classic Neural Architecture Search (NAS) techniques must repeat the search (and often the training) for every new target hardware platform, with an enormous computational cost that grows linearly with the number of devices to support.

## Key idea

Decouple training from architecture search: train a very large network once, designed to contain as sub-networks all candidate architectures (varying depth, width, kernel size, resolution), then for each device select the best sub-network with a lightweight search based on an accuracy and latency predictor, without retraining.

## Technical contribution

A "progressive shrinking" training technique that allows a single parent network to contain sub-networks of quality comparable to what they would have if trained from scratch; hardware-specific accuracy and latency predictors used to guide sub-network selection.

## Experimental methodology

Evaluation on ImageNet with deployment on different hardware platforms (mobile CPU, mobile GPU, microcontroller/edge devices), comparing accuracy and latency of the extracted sub-networks against models obtained from classic per-platform NAS.

## Results

Sub-networks extracted from OFA achieve accuracy comparable to platform-specific classic NAS, but with a drastic (orders of magnitude) reduction in overall search cost, since the expensive training is done only once.

## Comparison with the state of the art

Compared to traditional hardware-aware NAS (which repeats search+training for each target), OFA introduces the "train once, deploy everywhere" concept, becoming a reference for efficient NAS.

## Strengths

Drastic reduction in multi-platform search cost; code and pretrained models publicly released; influenced many later variants of efficient NAS.

## Weaknesses

Training the once-for-all parent network is still costly and complex to optimize (progressive shrinking requires an elaborate training pipeline); the latency predictors require profiling data specific to each new hardware target.

## Limitations

Validated mainly on image classification with CNN families; extension to different tasks (detection, audio, time series) or to very different architectures (Transformers) requires non-trivial adaptation.

## Open questions

How to extend the once-for-all paradigm to microcontrollers with extreme memory constraints (not just latency)? How well do latency predictors generalize to hardware never seen during the predictors' own training?

## Possible extensions

Once-for-all with an explicit static memory constraint for Cortex-M; combination with mixed-precision quantization to obtain already-quantized sub-networks ready for TinyML deployment.

## Relevance to our research

A key reference for research on hardware-aware NAS oriented to edge/embedded, especially when multiple target platforms need to be supported with a single training effort.

## Possible thesis topics

Extension of Once-for-All with an explicit memory-footprint constraint for microcontroller deployment; study of latency predictors on Cortex-M/RISC-V, underrepresented in the NAS literature.

## Possible collaborations

Research groups on efficient NAS (e.g. MIT HAN Lab, the original authors) and on hardware-aware benchmarks such as MLPerf Tiny.

## Links to related papers

[[2017_Howard_MobileNets]], [[2016_Han_DeepCompression]]
