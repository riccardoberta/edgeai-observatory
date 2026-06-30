# iCaRL: Incremental Classifier and Representation Learning

**Full citation:** Rebuffi, S.A., Kolesnikov, A., Sperl, G., Lampert, C.H. (2017). iCaRL: Incremental Classifier and Representation Learning. *IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017)*. https://openaccess.thecvf.com/content_cvpr_2017/html/Rebuffi_iCaRL_Incremental_Classifier_CVPR_2017_paper.html

**Linked concepts:** [[Continual_Learning]]

## Abstract summary

The authors propose iCaRL, a class-incremental learning method that learns new classes one batch at a time using only a small, bounded "exemplar" memory of representative examples from previously seen classes, combining nearest-class-mean classification with knowledge distillation to limit forgetting of old classes while learning new ones.

## Research problem

Standard deep classifiers catastrophically forget previously learned classes when trained sequentially on new classes without access to the full original training data, yet storing all past data is often impractical for memory-constrained or continually-deployed systems.

## Key idea

Maintain a small, fixed-size memory of exemplar images per class (selected via herding to best approximate the class mean in feature space), and when learning new classes, jointly (a) distill the old network's outputs on old-class exemplars into the updated network and (b) classify using nearest-mean-of-exemplars in the learned feature space rather than the network's own softmax output layer.

## Technical contribution

A combined architecture that learns the data representation and the classification rule jointly and incrementally, rather than assuming a fixed pretrained feature extractor; the use of a bounded exemplar memory together with distillation as the forgetting-mitigation mechanism, in contrast to purely regularization-based approaches that store no raw exemplars at all.

## Experimental methodology

Evaluated on class-incremental benchmarks (e.g. CIFAR-100 and ImageNet subsets) where classes are introduced in sequential batches, measuring classification accuracy across all classes seen so far after each incremental step, and comparing against fine-tuning-only baselines and other contemporary incremental-learning methods.

## Results

iCaRL substantially reduces catastrophic forgetting compared to naive fine-tuning and outperforms several contemporary incremental-learning baselines, maintaining reasonable accuracy across a growing number of classes even with a small, fixed exemplar memory budget.

## Comparison with the state of the art

Offers a memory-based alternative to purely regularization-based continual learning methods (e.g. Elastic Weight Consolidation); the two approaches are complementary, addressing the same forgetting problem with different mechanisms (constraining weight updates vs. retaining a bounded set of real examples plus distillation).

## Strengths

Works without needing to store the full historical dataset, scales gracefully to growing numbers of classes, and jointly addresses representation learning and classification rather than treating them separately.

## Weaknesses

Still requires storing some raw exemplar data (a privacy and memory consideration not present in purely regularization-based methods), and the exemplar memory budget grows (or each class's allotment shrinks) as more classes are added over time.

## Limitations

Evaluated mainly on image classification benchmarks; the memory and compute overhead of maintaining exemplars and performing distillation at each step has not been validated on memory-constrained edge/embedded hardware.

## Open questions

How small can the exemplar memory be made before forgetting becomes severe, particularly on devices with extremely limited storage? Can exemplar-free distillation-based methods close the accuracy gap with exemplar-based methods like iCaRL?

## Possible extensions

Combining exemplar-based class-incremental learning with model compression so that both the exemplar memory and the network itself fit within a microcontroller's storage budget; hybrid methods that combine iCaRL-style exemplar memory with weight-regularization approaches.

## Relevance to our research

A key complementary reference to weight-regularization continual learning methods in the [[Continual_Learning]] literature; relevant whenever the Observatory considers on-device class-incremental learning under tight storage constraints.

## Possible thesis topics

Adapting iCaRL's exemplar-memory mechanism to a microcontroller-class on-device learning pipeline, studying the accuracy/memory trade-off of exemplar count versus model compression ratio.

## Possible collaborations

Groups working on memory-efficient continual learning and on on-device training frameworks that must operate under hard storage limits.

## Links to related papers

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]]
