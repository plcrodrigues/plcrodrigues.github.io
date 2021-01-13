---
permalink: /code/
title:
excerpt: "Code"
author_profile: true
---

{% include base_path %}

<h1 style="margin-bottom:0.5em"><img src="/images/picto_code.svg" width="80px" style="margin-right:15px">Code</h1>

I am a strong believer that time spent sharing research code and datasets is never wasted. 
Here below I list some of the codes and projects that I have worked on.

<div class="container" style="padding-bottom:2em">
  <div class="row">
    <div class="col-3">
      <img src="/images/procrustes.svg" height="80px"/>
    </div>
    <div class="col-9">
      <span style="font-weight:bold;">Transfer Learning for BCI.</span> During my
      Ph.D. years, I worked a lot on problems related to transfer learning for 
      brain-computer interfaces. You can check the <a style="color:#00b050; font-weight:bold;" href="http://plcrodrigues.github.io/research/">research</a> page for an overview of this topic. The code related to RPA is available <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/RPA" target="_blank">here</a> and the
      code related to the Dimensionality Transcending is <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/DT" target="_blank">here</a>. Please feel free to open issues on both repositories; contributions are always welcome.      
    </div>
  </div>
</div>

<div class="container" style="padding-bottom:2em">
  <div class="row">
    <div class="col-3">
      <img src="/images/spd_manifold.svg" height="80px"/>
    </div>
    <div class="col-9">
      <span style="font-weight:bold;">pyRiemann.</span> In this package developed by
      <a style="color:#00b050; font-weight:bold;" href="https://alexandre.barachant.org/" target="_blank">Alexandre Barachant</a> you can find implementations of most of the basic geometric operations in the symmetric-positive
      definite manifold. A very nice feature of <a style="color:#00b050; font-weight:bold;" href="https://pyriemann.readthedocs.io/en/latest/" target="_blank">pyRiemann</a> is its compatibility with the <a style="color:#00b050; font-weight:bold;" href="https://scikit-learn.org/stable/" target="_blank">scikit-learn</a> API. I did some contributions to the code base of this package, mainly on its non-linear dimensionality reduction features.
    </div>
  </div>
</div>

<div class="container" style="padding-bottom:2em">
  <div class="row">
    <div class="col-3">
      <img src="/images/moabb.png" height="80px"/>
    </div>
    <div class="col-9">
      <span style="font-weight:bold;">MOABB.</span> A recent effort in improving the reproducibility of the research in brain-computer interfaces (BCI) has been the development of the <a style="color:#00b050; font-weight:bold;" href="http://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB</a> framework. It provides the means for easily comparing classification methods on a benchmark of publicly available BCI datasets with an API compatible with <a style="color:#00b050; font-weight:bold;" href="https://scikit-learn.org/stable/" target="_blank">scikit-learn</a> and <a style="color:#00b050; font-weight:bold;" href="https://mne.tools/stable/index.html" target="_blank">MNE</a>. I have contributed to its code base with the inclusion of the functionality for handling BCI data in the P300 paradigm. I have also co-organized a one-day workshop at the Graz BCI 2019 conference with a hands-on tutorial to MOABB. The code and slides for the workshop are available <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/Workshop-MOABB-BCI-Graz-2019" target="_blank">here</a>.      
    </div>
  </div>
</div>

<div class="container" style="padding-bottom:2em">
  <div class="row">
    <div class="col-3">
      <img src="https://www.sciencesetavenir.fr/assets/afp/2017/11/24/79e672d731e751c4dd2970edf0fe693ff415bdad.jpg" height="80px"/>
    </div>
    <div class="col-9">
      <span style="font-weight:bold;">Public EEG datasets.</span>  I have co-created a set of nine publicly available datasets with EEG recordings of several experiments at the GIPSA-lab in Grenoble, France. I have contributed to the writing of all technical reports and have created several github repositories with minimal working examples, showing how researchers can easily download each dataset and use it for their own data analysis. Here below you find the list of names of these datasets along with links to their documentation and github repository.
      <ul style="margin-top:0.5em">     
        <li>Brain Invaders calibration-less P300-based BCI with modulation of flash duration Dataset (bi2015a)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02172347" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/3266930#.X_wPr1NKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2015a-GIPSA" target="_blank">code</a>.
        </li>
        <li>Brain Invaders Cooperative versus Competitive: Multi-User P300- based Brain-Computer Interface Dataset (bi2015b)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02173913" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/3268762#.X_wPRlNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2015b-GIPSA" target="_blank">code</a>.
        </li>
        <li>Brain Invaders calibration-less P300-based BCI using dry EEG electrodes Dataset (bi2014a)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02173913" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/3266223#.X_wPeVNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2014a-GIPSA" target="_blank">code</a>.
        </li>
        <li>Brain Invaders Solo versus Collaboration: Multi-User P300-based Brain-Computer Interface Dataset (bi2014b)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02173958v1" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/3267302#.X_wRZ1NKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2014b-GIPSA" target="_blank">code</a>.
        </li>
        <li>Brain Invaders Adaptive versus Non-Adaptive P300 Brain-Computer Interface dataset (bi2013)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02126068" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/2669187#.X_wQcFNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2013-GIPSA" target="_blank">code</a>.          
        <li>Building Brain Invaders: EEG data of an experimental validation (bi2012)
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02126068" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/2649069#.X_wQJVNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.BI.EEG.2012-GIPSA" target="_blank">code</a>.
        </li>            
        <li>Passive Head-Mounted Display Music-Listening EEG dataset
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02085118" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/2617085#.X_wQsVNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.PHMDML.EEG.2017-GIPSA" target="_blank">code</a>.
        </li>    
        <li>Dataset of an EEG-based BCI experiment in Virtual Reality and on a Personal Computer
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02078533" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/2605205#.X_wQ6VNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.VR.EEG.2018-GIPSA" target="_blank">code</a>.
        </li>     
        <li>EEG Alpha Waves Dataset
        <br>
        Links: <a style="color:#00b050; font-weight:bold;" href="https://hal.archives-ouvertes.fr/hal-02086581" target="_blank">documentation</a>,
        <a style="color:#00b050; font-weight:bold;" href="https://zenodo.org/record/2605110#.X_wRHVNKjM0" target="_blank">data</a>, and
        <a style="color:#00b050; font-weight:bold;" href="https://github.com/plcrodrigues/py.ALPHA.EEG.2017-GIPSA" target="_blank">code</a>.
        </li>                                   
