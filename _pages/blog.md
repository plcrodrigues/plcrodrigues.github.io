---
permalink: /blog/
title:
excerpt: "Blog"
author_profile: true
use_math: true
---

{% include base_path %}

<h1 style="margin-bottom:0.5em"><img src="/images/picto_blog.svg" width="80px" style="margin-right:15px">Blog</h1>

# The Riemannian Gaussian distribution
With Salem Saïd I've been working a lot on how to sample from the Riemannian Gaussian
distribution, a generalized version of our favorite probability distribution to the
space of symmetric positive definite matrices.

More precisely, the pdf looks like this: for $\boldsymbol{X} \in \mathcal{P}(d)$ we have

$$
p(\boldsymbol{X}) = \dfrac{1}{\zeta(\sigma)}\exp\left(-\dfrac{1}{2\sigma^2}\delta_R^2(\boldsymbol{X}, \boldsymbol{I})\right)
$$
