# Edge Impulse

Edge Impulse is a commercial MLOps (machine-learning-operations) platform: it handles data collection, labeling, training, optimization, and hardware-specific deployment through one workflow. Unlike this Observatory's other Frameworks concepts, which are runtimes or compilers operating at the model-execution layer ([[TensorFlow_Lite_Micro]], [[CMSIS-NN]], [[microTVM_TVM]], [[MLIR]], [[ONNX_Runtime]], [[ExecuTorch]]), Edge Impulse sits one layer above them, ultimately targeting those lower-level runtimes for the actual on-device execution.

## Evolution of the concept

Edge Impulse's founding paper (Hymel et al., 2022) documents the platform's motivation and, as of October 2022, its real-world scale: 118,185 projects and 50,953 developers, making it one of the most widely adopted MLOps platforms in practical TinyML development.

## Key papers

[[2022_Hymel_EdgeImpulse]] — introduces Edge Impulse as a cloud-based MLOps platform addressing TinyML's fragmented software/hardware landscape; co-authored by a mix of Edge Impulse's own team and academic/industry researchers, including Pete Warden (see [[2018_Warden_SpeechCommands]]).

## Open problems

How does a model deployed through Edge Impulse's automated optimization pipeline compare, on identical hardware, to the same model manually optimized and deployed via [[TensorFlow_Lite_Micro]] or [[CMSIS-NN]] directly — does the platform's ease of use and portability trade off measurable performance? How has the platform's capability and adoption evolved since the October 2022 snapshot reported in its founding paper?

## Research ideas

A controlled benchmark comparing Edge Impulse's automated pipeline against manual [[TensorFlow_Lite_Micro]]/[[CMSIS-NN]] deployment for the same model and target hardware, to quantify any performance gap traded for the platform's portability.

## Possible thesis topics

A performance/portability benchmark of Edge Impulse's automated pipeline against manual runtime-specific deployment for one of this Observatory's tracked Applications, for example [[Keyword_Spotting]] or [[Human_Activity_Recognition]] (Master's).

## Links

[[TensorFlow_Lite_Micro]], [[CMSIS-NN]], [[Keyword_Spotting]]
