---
permalink: /research/
excerpt: "Research"
author_profile: true
---

<h1 style="margin-bottom:0.5em"><img src="/images/picto_research.svg" width="60px" style="margin-right:15px">Research</h1>

In this page, I summarize some of the research topics that I've investigated during my career. You can also check the <a href="/publications/" style="color:#00b050; font-weight:bold;">publications</a> page for a full list of my published papers. Please feel free to contact me if you would like to discuss further some of these research topics.

<div>
<h2>Simulation-based inference 
<a data-toggle="collapse" href="#collapse1" role="button" aria-expanded="false" aria-controls="collapse1" style="color:#00b050; font-weight:bold; font-size:0.65em; vertical-align: middle;">(see more)</a>
</h2>
<p>
<a data-toggle="collapse" href="#collapse1" role="button" aria-expanded="false" aria-controls="collapse1">
<img src="/images/research_sbi.svg" style="float: left; padding-bottom:1em; padding-top:0.05em"/></a>
</p>
<p class="collapse" id="collapse1">
<!-- Bayesian inference on modern complex simulator models is in general a difficult task because the likelihood function of the model’s output is often intractable. Simulation-based inference (SBI) bypasses such obstacle by <span style="color:#00b050">approximating the posterior distribution</span> using a flexible function (e.g. a neural network) trained over simulations on different parameters. -->
Inferring the laws and parameters that drive physical systems has been a long standing issue across all natural sciences. Whereas the methodology for building models from first principles may vary from one field to the other, <span style="font-weight:bold">estimating the parameters that best fit a given observation</span> is an inverse problem for which general methods can be used. A common approach in practice is to perform parameter sweeps over a simulator until finding an output that is sufficiently similar to a given observation.
<br><br>
Although easily implemented and rather intuitive, such procedures are time consuming and are usually incapable of characterizing sets of parameters for which the simulator generates the same output. Alternatively, one can use <span style="font-weight:bold">Bayesian inference</span>, a powerful framework that yields a posterior probability density function describing how likely each set of parameters is of having generated a given observed data. This posterior distribution can then be used in <span style="font-weight:bold">various tasks</span>, such as assessing the variance of the parameter estimation or characterizing the indeterminacies of the model.
<br><br>
Unfortunately, Bayesian inference on modern complex simulator models is in general a difficult task because the likelihood function of the model’s output is often difficult or impossible to obtain. A modern approach for bypassing such obstacle is to use <span style="font-weight:bold">simulation-based inference (SBI)</span> methods, which draws on several simulations of the model with different parameters to learn an approximation of the posterior distribution from examples. The first works on SBI are also known as approximate Bayesian computation (ABC) and have been applied to invert models from ecology, population genetics, and epidemiology. Recently, there has been a <span style="font-weight:bold">growing interest in the machine learning community</span> in improving the limitations of ABC, which include the large number of simulations required for approximating the posterior distribution, the pre-definition of summary statistics to describe the observed data, and the need of defining a distance function to compare the results of two simulations. The figure above illustrates how the posterior distribution estimated via SBI might be used to infer the parameters generating a given observation $x_o$.
<br><br>
Some of the topics related to SBI that I've been working on recently are:
- Validating posterior approximations in the SBI setting.
- The effects of model misspecification in SBI and how to counter them.
- Using the score diffusion framework in SBI.
</p>
</div>

<div>
<h2>Exploring invariances of multivariate time series 
<a data-toggle="collapse" href="#collapse2" role="button" aria-expanded="false" aria-controls="collapse2" style="color:#00b050; font-weight:bold; font-size:0.65em; vertical-align: middle">(see more)</a>
</h2>
<p>
<a data-toggle="collapse" href="#collapse2" role="button" aria-expanded="false" aria-controls="collapse2">
<img src="/images/research_phd.svg" style="float: left; padding-top:0.10em"/></a>
</p>
<p class="collapse" id="collapse2">
A multivariate time series represents measurements obtained from a set of sensors as a collection of vectors indexed by time. A common way for analysing such data is to estimate a set of parameters that describes its statistical behavior, such as its mean vector, its auto-covariance matrices, or its cross-spectral density matrices. Two multivariate time series may then be compared by defining a distance between the sets of parameters describing their statistics. A principled way for doing so is to <span style="font-weight: bold">study the intrinsic geometry of the space</span> where the parameters are defined and use the geodesic distance between them as a measure of similarity. Such approach is based on concepts borrowed from Riemannian geometry (RG) and allows us to <span style="font-weight: bold">manipulate multivariate time series as points in a metric space</span>. A convenient outcome of this approach is that it allows the development of new algorithms inspired by intuitive geometric arguments, as well as a new understanding of classical algorithms that were firstly developed in a purely analytical form and that can be reinterpreted under the RG framework.
<br><br>
I have used this geometric framework to <span style="font-weight:bold">explore invariances in multivariate time series</span>. An invariance is “a property that remains unchanged regardless of changes in the conditions of measurements”. This is a very powerful property of a system, which reflects a notion of stability that is intrinsic to the dynamical system under study and that allows for a <span style="font-weight:bold">profound interpretation of its behavior</span>. Invariances are at the core of many scientific fields, such as in classical mechanics, where the laws of motion are the same in all inertial frames (also known as Galilean invariance), and electromagnetism, where invariances and symmetries are commonly used to determine expressions describing electric and magnetic fields. The figure above illustrates these concepts with an example in astronomy.
<br><br>
In the context of multivariate time series, invariances may be related to different aspects of the phenomena that they represent. For instance, the statistical distribution of samples
gathered from <span style="font-weight:bold">different experimental sessions</span> are usually different, hindering their joint analysis with classical statistical methods. However, if the experiments portray the same phenomena, it is reasonable to assume that the samples of each session share invariant features. A concrete example is in EEG-based <span style="font-weight:bold">brain-computer interfaces (BCI)</span>, where the data from two subjects carrying out the same cognitive tasks, i.e., the same BCI paradigm, may have very different statistical distributions, even if latent information is clearly shared. Based on these observations, I have proposed an original algorithm that uses the RG framework to adapt the statistics of mismatched datasets and makes their joint analysis possible. This method is an <span style="font-weight:bold">extension of the classical Procrustes analysis</span> from statistical shape analysis, which applies rigid transformations to data points (i.e., translation, stretching and rotation) from two datasets in order to match their statistical distributions. These transformations are carried out on points defined in a Riemannian manifold and is, therefore, called the Riemannian Procrustes analysis (RPA).

</p>
</div>

<!-- <div>
<h2>Neural connectivity estimation 
<a data-toggle="collapse" href="#collapse3" role="button" aria-expanded="false" aria-controls="collapse3" style="color:#46B1C9; font-weight:bold; font-size:0.8em; vertical-align: middle">(see more)</a>
</h2>
<p>
<a data-toggle="collapse" href="#collapse3" role="button" aria-expanded="false" aria-controls="collapse3">
<img src="/images/research_pdc.svg" style="float: left;"/></a>
</p>
<p class="collapse" id="collapse3">
Characterizing neural connectivity has become central to <span style="color:#00b050">understanding the brain</span>
and its status under different stimulus and/or behavioural conditions. Amidst the diversity of currently available
approaches, those based on modeling stationary multivariate time series remain the most popular ones thanks to the wide avaliability of off-the-shelf linear modeling routines and decades of practical experience. 
</p>
</div> -->
