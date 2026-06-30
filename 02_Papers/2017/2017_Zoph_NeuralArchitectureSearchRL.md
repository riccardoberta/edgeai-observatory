# Neural Architecture Search with Reinforcement Learning

**Full citation:** Zoph, B., Le, Q.V. (2017). Neural Architecture Search with Reinforcement Learning. *5th International Conference on Learning Representations (ICLR 2017)*. https://openreview.net/forum?id=r1Ue8Hcxg

**Linked concepts:** [[NAS]]

## Abstract summary

The authors train a recurrent neural network ("controller") with reinforcement learning to generate descriptions of candidate neural network architectures; each generated architecture is trained on the target task, and its validation accuracy is used as the reward signal to update the controller, so that over many iterations the controller learns to generate increasingly accurate architectures.

## Research problem

Designing high-performing neural network architectures (number of layers, layer types, hyperparameters, connectivity) had been a largely manual, expert-driven and trial-and-error process; the paper asks whether this design process itself can be automated and learned.

## Key idea

Treat architecture design as a sequential decision-making problem: the controller RNN outputs the architecture description one design choice at a time (like a sequence of tokens), and policy-gradient reinforcement learning (REINFORCE) is used to push the controller toward generating architectures that, once trained, achieve higher validation accuracy.

## Technical contribution

The framing of architecture search as a reinforcement learning problem with the validation accuracy of a fully trained candidate network as the reward; a working controller-and-child-network training loop, applied both to standard feedforward CNN architectures for image classification and to recurrent cell architectures for language modeling, naming the field "Neural Architecture Search" in the process.

## Experimental methodology

The controller proposes thousands of candidate architectures over the course of search, each of which is actually trained (partially or fully) to obtain a validation accuracy used as the reward; final discovered architectures are evaluated on CIFAR-10 (image classification) and on a language modeling benchmark, and compared to hand-designed architectures and to architectures from other automated/random search methods of the time.

## Results

The architectures discovered by the RL controller match or exceed the accuracy of the best hand-designed human architectures on CIFAR-10 and discover novel, competitive recurrent cell designs for language modeling, demonstrating that automated search can rival expert architecture design.

## Comparison with the state of the art

At the time, this outperformed prior, more limited automated search approaches (e.g. random search, simple evolutionary methods) and was competitive with or better than the best manually designed architectures, establishing reinforcement-learning-based search as a viable and influential paradigm.

## Strengths

Demonstrated for the first time that an automated, learned search process could discover architectures competitive with the best human-engineered designs across two very different task types (vision and language).

## Weaknesses

Extremely computationally expensive — training thousands of full candidate networks from scratch to generate each reward signal requires very large compute budgets, far beyond what most research groups or edge-focused applications could afford.

## Limitations

The search cost makes the original method impractical for direct use on resource-constrained hardware targets, and it optimizes for accuracy alone, without any notion of latency, memory, or energy cost on a deployment device.

## Open questions

How can the search cost be reduced by orders of magnitude (e.g. via weight sharing across candidates, proxy tasks, or differentiable search) while preserving search quality? How can hardware cost (latency, memory, energy) be incorporated directly into the search objective rather than optimizing for accuracy alone?

## Possible extensions

Weight-sharing and differentiable search methods (e.g. ENAS, DARTS) that cut search cost dramatically; hardware-aware NAS that adds latency/energy terms to the reward, directly relevant to searching architectures for microcontroller-class hardware.

## Relevance to our research

The founding paper of the NAS field; an essential historical reference whenever the Observatory discusses hardware-aware or efficiency-aware architecture search for edge devices, since all such later work inherits this paper's core RL-search framing.

## Possible thesis topics

Reproducing a small-scale RL-based architecture search with an added latency/energy term in the reward, targeting a Cortex-M-class deployment, and comparing search cost and resulting accuracy/efficiency trade-off against a modern differentiable hardware-aware NAS method.

## Possible collaborations

Groups working on differentiable and hardware-aware NAS, and on efficient search methods (weight sharing, proxy tasks) for compute-constrained research settings.

## Links to related papers

[[2017_Howard_MobileNets]]
