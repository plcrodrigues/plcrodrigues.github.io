---
permalink: /research/
title: 
excerpt: "Research"
author_profile: true
redirect_from: 
  - /research/
  - /research.html
---

In this page I summarize some of the research questions that I've investigated 
up to today. Please feel free to **contact me** if you would like to discuss 
further some of these topics.

## Simulation-based inference

Bayesian inference on modern complex simulator models is in general a difficult 
task because the likelihood function of the model’s output is often intractable. 
A modern approach for bypassing such obstacle is to use *simulation-based inference* (SBI)
methods, in which a flexible function (e.g. a neural network) learns how to 
approximate the posterior distribution based on simulations over different parameters. I've been
mostly interested in how to apply such methods to non-linear models coming from computational neuroscience.

## Exploring invariances of multivariate time series

Multivariate time series are the standard tool for describing and analysing 
measurements from multiple sensors during an experiment. I've been interested in
mathematical representations that are invariant to transformations occurring in
practical situations, such as changes in instrument calibration and different experimental
setups for measuring the same phenomenon. The main source of inspiration for most 
of my works have been experiments with neural signals from electroencephalography 
(EEG), but these ideas are amenable to other kinds of time series.

## Neural connectivity estimation

Characterizing neural connectivity has become central to understanding the brain 
and its status under different stimulus and/or behavioural conditions. So much 
so that it has been the focus of an almost endless number of approaches with 
different levels of rigour. Amidst the diversity of currently available
approaches, those based on modeling stationary multivariate time series remain 
the most popular ones thanks to the wide avaliability of off-the-shelf linear
modeling routines and decades of practical experience.
