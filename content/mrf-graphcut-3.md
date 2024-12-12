Title: Markov Random Field (MRF) and Graph-Cut (3)
Category: Computing
Date: 2011-11-08 10:08
Tags: PhD, Math, English
Latex:


---

本文是《MRF GraphCut系列》系列的一部分：

* [Markov Random Field (MRF) and Graph-Cut (1)](/mrf-graphcut-1.html)
* [Markov Random Field (MRF) and Graph-Cut (2)](/mrf-graphcut-2.html)
* Markov Random Field (MRF) and Graph-Cut (3)（本文）

---

<style>.centered { max-width: 400px; display: block; margin-left: auto; margin-right: auto } </style>

Implemented Loopy Belief Propagation [[wiki]](http://en.wikipedia.org/wiki/Belief_propagation), which is a more general optimization approach for Markov Random Field [[post 1]](https://grapeot.me/markov-random-field-mrf-and-graph-cut-1.html) [[post 2]](https://grapeot.me/markov-random-field-mrf-and-graph-cut-2.html).
Different from Graph Cut, it can be extended easily for non-grid graphs and non-binary cases. Here are some experiment results on binary and gray-scale image restoration.

Some experiment results:

<img class="centered" src="/images/mrf_noisy_small.jpg" alt="" />

<img class="centered" src="/images/mrf_lbp_result.jpg" alt="" />

<img class="centered" src="/images/mrf_penguin.png" alt="" />

<img class="centered" src="/images/mrf_penguin_lbp.png" alt="" />

Updates:

Another interesting direction for image denoising is convex optimization, such as total-variation minimization.
A more detailed discussion can be found [here](/thoughts-about-convex-optimization.html).