---
title: 'Plotting 2x2 SPD matrices'
author_profile: false
date: 2023-06-30
permalink: /posts/plotting-spd-matrices/
tags:
  - SPD matrices
  - Riemannian Geometry 
---

{% include base_path %}

## Introduction
In this short note, I want to show you how we can plot data points defined in the 
symmetric positive definite (SPD) manifold. This can be useful when doing 
illustrative examples or pedagogical explanations for algorithms applied to 
this sort of data. I will focus on the case of $2 \times 2$ matrices because 
it is the only situation in which the plots are **exact**, i.e. without any
distortion. For higher dimensional data, one should recur to one of the several 
algorithms for non-linear dimensionality reduction (e.g. t-SNE, MDS, PCA, 
Laplacian eigenmaps, etc). I was inspired to write this note after trying to reproduce Figure 1 from 
<a href="https://arxiv.org/abs/1807.10479" style="color:#00b050; font-weight:bold;">this</a> article for my presentation about `pyriemann` for the BCI meeting 2023 [<a href="https://github.com/mccorsi/BCI-2023-Open-Source-Tool-workshop/tree/main/Pyriemann" style="color:#00b050; font-weight:bold;">link</a>].

## SPD matrices
The most natural way of parametrizing a $2 \times 2$ SPD matrix  is to write

$$
\boldsymbol{X} = \left[\begin{array}{cc}a & b \\ b & c\end{array}\right]~,
$$

which clearly can be displayed in a three-dimensional plot. Sweeping different 
values $(a_i, b_i, c_i)$ will yield different matrices matrices 
$\boldsymbol{X}_i$, but to ensure that they are all SPD, they have to respect
that $a_i c_i - b_i^2 > 0$.

Respecting such condition is not necessarily very intuitive, so a different
parametrization for the SPD matrices can be

$$
\boldsymbol{X} = \left[\begin{array}{cc}\cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta)\end{array}\right]\left[\begin{array}{cc}\lambda_1 & 0 \\ 0 & \lambda_2\end{array}\right]\left[\begin{array}{cc}\cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta)\end{array}\right]^\top~,
$$

where $\theta \in [0, 2\pi]$ and $\lambda_1, \lambda_2 > 0$ will ensure that $\boldsymbol{X}$ is SPD.

## What to plot?
[...]

## An example
[...]

{% highlight python %}
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
{% endhighlight %}

[...]

<center><img src="/codes/rejection-sampling-fig02.svg" style="height:200%;"></center>

[...]

## Conclusion
[...]
