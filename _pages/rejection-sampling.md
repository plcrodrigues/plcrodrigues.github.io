---
title: 'How does rejection sampling work?'
author_profile: false
date: 2023-06-24
permalink: /posts/rejection-sampling/
tags:
  - Statistics
  - SPD matrices
  - Riemannian Geometry 
---

{% include base_path %}

## Introduction
I've been recently interested in the inner workings of the well known <a href="https://en.wikipedia.org/wiki/Rejection_sampling" style="color:#00b050; font-weight:bold;">rejection sampling</a> procedure for obtaining samples from a probability distribution
function (pdf). This is a nice sampling procedure that only returns samples that follow
**exactly** the target pdf, as opposed to usual MCMC schemes for which one has to
wait for the chains to converge before being sure that the samples really follow the distribution that we want to sample. The downside of rejection sampling is that it usually
does not scale well when the data dimension increases, but we won't be bothering
too much about this for now. 

There are many excellent references for learning and
understanding how rejection sampling works, my favorite being Christian Robert and George
Casella's book "Monte Carlo Statistical Methods". In what follows, I tried to
give a somewhat intuitive and pedagogical explanation of the basic version of
the rejection sampling method. I've also included an example written in `python`.

## Problem statement
Suppose we want to sample a continuous random variable with distribution $F$ 
and pdf $f$, but it is not a simple transformation from other random variables
and we have no idea of how to obtain the inverse of its cdf (in which case we
could use the <a href="https://en.wikipedia.org/wiki/Inverse_transform_sampling" style="color:#00b050; font-weight:bold;">inverse transform sampling </a> method). 
We have, however, access to another distribution $G$ with pdf $g$ from which 
samples can be obtained very easily. We also know that $\forall x \in \text{supp}(f)$ 
there is a constant $M$ for which

$$
f(x) \leq M~g(x)~.
$$

**Question**: Can we use samples from $g$ to get samples from $f$?

## Theory

We will consider now a result that, at first, seems quite artificial, but it is
in fact very useful for what we will be doing next: if we sample $X \sim g$ and 
$U \sim \mathcal{U}[0, 1]$ independently, we can always write that

$$
\text{Prob}\left(U \leq \dfrac{f(X)}{M g(X)} \Bigg|~X = x \right) = \dfrac{f(x)}{M~g(x)}~.
$$

> This is not hard to see if you remember two basic things: (1) When 
> conditioning on $X = x$, we are saying that the right side of the inequality 
> is a **constant**. (2) The probability of an uniform random variable $U$ being 
> smaller than a fixed constant $u$ is **exactly** equal to $u$.

Now, if we take the integral of the above conditional probability over all 
possible values of $x$ we obtain an **unconditioned** probability statement as per

$$
\int \text{Prob}\left(U \leq \dfrac{f(X)}{M g(X)} \Bigg|~X = x \right)~g(x)\mathrm{d}x = \int \dfrac{f(x)}{M}~\mathrm{d}x = \dfrac{1}{M}
$$

since $f$ is a pdf and thus sums up to one. We will rewrite this result as

$$
\boxed{\text{Prob}_G\left(U \leq \dfrac{f(X)}{M g(X)} \right) = \dfrac{1}{M}}
$$

where the subscript in the $\text{Prob}_G$ operator indicates that the random 
variable $X$ is sampled from the distribution G with corresponding pdf $g$.

Another important result is that, for any measurable set $\mathcal{B}$ in the 
space where $X$ is defined, Bayes' theorem gives us

$$
\text{Prob}_G\left(X \in \mathcal{B}~\Bigg|~U \leq \dfrac{f(X)}{M~g(X)}\right) = \dfrac{\text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)},~X \in \mathcal{B}\right)}{\text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)}\right)}
$$

The numerator for this expression can be rewritten as

$$
\begin{array}{rcl}
\text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)},~X \in \mathcal{B}\right) &=& \displaystyle\int_{\mathcal{B}} \text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)} ~\Bigg|~X = w\right)~g(w)\mathrm{d}w \\[1em]
&=& \displaystyle\int_\mathcal{B} \dfrac{f(w)}{Mg(w)}~g(w)\mathrm{d}w \\[1em]
&=& \dfrac{1}{M} \times \text{Prob}_F\Big(X \in \mathcal{B}\Big)
\end{array}
$$

and dividing by the denominator we end up with

$$
\boxed{\text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)},~X \in \mathcal{B}\right) = \text{Prob}_F\Big(X \in \mathcal{B}\Big)}
$$

This is a very nice result because we have a probability statement written for
a random variable $X$ sampled from $G$ (i.e. the distribution which is easy to 
sample from) equated to another statement for a random variable sampled from $F$. 
These two statements are linked through the same set $\mathcal{B}$.

## The algorithm
Using the above results, we can derive the following **algorithm** to obtain 
samples from a target distribution $F$ with pdf $f$:

1. Generate a random variable $X \sim g$

2. Generate a random variable $U \sim \mathcal{U}[0, 1]$ independently from $Y$

3. If we have that
   
   $$
   U \leq \dfrac{f(X)}{M~g(X)}
   $$

   then accept the sample; otherwise, reject it and go back to **Step 1**.

The samples that will get accepted in this algorithm are those for which 
the inequality holds. Their distribution function is

$$
\forall \mathcal{B} \quad \text{Prob}_G\left(X \in \mathcal{B}~\Bigg|~U \leq \dfrac{f(X)}{M~g(X)}\right) = \text{Prob}_F\left(X \in \mathcal{B}\right)
$$

meaning that they follow the distribution $F$ that we wanted from the start.

## Bonus: acceptance probability
As the name says, the rejection sampling algorithm relies on a rejection
procedure that filters out samples from $G$ that can not be considered as coming
from $F$. As such, knowing upfront how many candidate samples from $G$ are necessary **in average** so to get a prescribed number of samples from $F$ is very useful. 

Since the accepted samples are those for which the inequality in Eq (8) is true,
we can state that

$$
\text{Prob}(X \text{ is accepted}) = \text{Prob}_G\left(U \leq \dfrac{f(X)}{M~g(X)}\right) = \dfrac{1}{M}~,
$$

which gives us the intuitive result that the probability of acceptance decreases
for larger values $M$. Therefore, upper bounding the pdf $f$ by a poorly chosen
$g$ for which $M$ is large will result in an algorithm with many rejections.

## An example
In a recent project involving the sampling of symmetric positive definite
matrices from a <a href="https://arxiv.org/abs/1507.01760" style="color:#00b050; font-weight:bold;">Riemannian Gaussian</a> distribution,
I've stumbled upon the following two-dimensional pdf

$$
f(r_1, r_2) = \dfrac{1}{\zeta_2(\sigma)}\exp\left(-\frac{1}{2\sigma^2}(r_1^2 + r_2^2)\right)\sinh\left(\dfrac{r_1 - r_2}{2}\right) \times \mathbf{I}(r_1 - r_2 \geq 0)
$$

where $\mathbf{I}(a \geq 0)$ is the indicator function for $a \geq 0$. The
normalization constant $\zeta_2(\sigma)$ is known but rather complicated to
write, but we will see that we won't even need it for our rejection sampling
procedure.

The 2D plot for this pdf is given below.

<center><img src="/codes/rejection-sampling-fig01.svg"></center>

It is not too <a href="https://github.com/pyRiemann/pyRiemann/pull/198" style="color:#00b050; font-weight:bold;">hard to show</a> that the target pdf can be upper bounded as per

$$
f(r_1, r_2) \leq \dfrac{\pi \sigma^2 \exp(\sigma^2/4)}{\zeta_2(\sigma)} g(r_1, r_2)
$$

where $g(r_1, r_2) = \mathcal{N}(\mu, \Sigma)$ with $\mu = \left[\tfrac{1}{2}\sigma^2, -\tfrac{1}{2}\sigma^2\right]^\top$ and $\Sigma = \sigma^2\mathbf{I}_2$.

The testing criterium appplied to $(R_1, R_2) \sim g$ and $U \sim \mathcal{U}[0, 1]$ can then be written as

$$
U \leq {\exp(-\sigma^2/4)}  \times \dfrac{\zeta_2(\sigma)f(R_1, R_2)}{\pi \sigma^2g(R_1, R_2)}~,
$$

where we see that the $\zeta_2(\sigma)$ in the numerator of the second term will cancel out with the one inside
the expression for $f$, meaning that we won't even have to bother to calculate it.

An example of `python` implementation for the rejection sampling in this case is:

{% highlight python %}
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

# define the unnormalized version of the target pdf f
def pdf_f_unnormalized(r, sigma):
    y = np.exp(-(r[:,0]**2 + r[:,1]**2)/(2*sigma**2))
    y = y * np.sinh((r[:,0] - r[:,1])/2)
    y = y * ((r[:,0] - r[:,1]) > 0)
    return y

sigma = 1 # fix the dispersion of the target pdf f
N_samples = 10_000 # how many samples we wish to have
N_cand = 10_000 # how many candidate samples for each iteration

# run a while loop to get the desired total number of samples
R_samples = []
N_cand_total = 0
while len(R_samples) < N_samples:
    # setting up the proposal pdf g
    mu = np.array([1/2*sigma**2, -1/2*sigma**2])
    cov = sigma**2*np.eye(2)    
    # get samples from g
    R_cand = multivariate_normal.rvs(mu, cov, size=N_cand)
    # get uniform samples
    U = np.random.rand(N_cand)
    # set up the test criterium
    num = np.exp(-sigma**2/4) * pdf_f_unnormalized(R_cand, sigma)
    den = np.pi*sigma**2 * multivariate_normal.pdf(R_cand, mu, cov)
    # get the idx of the candidate samples that pass the test
    sel = U < num/den
    R_accept = R_cand[sel]
    # append the samples
    R_samples = R_samples + list(R_accept)
    # monitor the total number of candidate samples
    N_cand_total = N_cand_total + N_cand

# estimate the probability of acceptance
prob_acceptance = len(R_samples) / N_cand_total
# ensure that we only keep the desired number of samples
R_samples = np.stack(R_samples[:N_samples])
{% endhighlight %}

The figure below overlays the target pdf $f$ with the 2D histogram of the
samples obtained via rejection sampling. We see that the samples tend to 
concentrate where the pdf is larger and they respect the strong constraint of
always having $r_1 - r_2 \geq 0$. 

<center><img src="/codes/rejection-sampling-fig02.svg"></center>

We can also inspect the probability of acceptance of the rejection sampling
procedure for different values of $\sigma$. The theoretical values in the plot
below were obtained using a numerical approximation of $\zeta_2(\sigma)$. We
see that the probability of acceptance increases up to the point were it stabilizes
at half. This comes at no surprise, since we can expect that the target pdf $f$
will look more and more similar to the gaussian proposal $g$ as $\sigma$ increases and,
therefore, more samples will have the tendency to be accepted. Things stabilize
at a probability of 0.5 because of the influence of the indicator function
imposing that $r_1 - r_2 \geq 0$, i.e. half of the samples always get thrown away.

<center><img src="/codes/rejection-sampling-fig03.svg"></center>

## Conclusion
That's it for today, folks! We have seen a derivation of the main results that
allow us to understand how and why the rejection sampling algorithm works. I've
included a non-trivial example with some `python` code in the hope of providing
a clear example of how the method can be used in practice.