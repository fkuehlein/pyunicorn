title: 'pyunicorn v1.0: An established Python toolbox for complex systems science'
tags:
  - Python
  - complex systems
  - networks
  - timeseries analysis
authors:
  - given-names: Fritz
    surname: Kühlein
    orcid: 0009-0006-7513-0688
    corresponding: true
    affiliation: "1, 2, 6"
  - given-names: Boyan
    surname: Beronov
    affiliation: "1, 3"
  - given-names: Max
    surname: Bechtold
    affiliation: "1, 2, 6"
  - given-names: Reik V.
    surname: Donner
    affiliation: "1, 4"
  - given-names: Jonathan F.
    surname: Donges
    affiliation: "1, 2, 4"
affiliations:
 - name: Earth Resilience Science Unit, Potsdam Institute for Climate Impact Research, Member of the Leibniz Association,
Telegrafenberg A31, D-14473 Potsdam, Germany
   index: 1
 - name: Max Planck Institute of Geoanthropology, Germany
   index: 2
 - name: Boyan's affiliation (if applicable)
   index: 3
 - name: Magdeburg-Stendal University of Applied Sciences, Germany
   index: 4
 - name: Stockholm Resilience Center, Sweden
   index: 5
 - name: Institute of Physics and Astronomy, University of Potsdam, D-14476 Potsdam, Germany
   index: 6
date: 10 March 2026
bibliography: paper.bib
---


# Summary

Pyunicorn is a toolbox for complex systems analysis that is written in Python and C. The package contains implementations of highly specialised methods that derive from the synthesis of network theory and time series analysis, but can also serve as a general-purpose tool for the construction of complex networks. Pyunicorn is fast, as computationally expensive functions are written in C or precompiled via [Cython](https://cython.org). It can easily be parallelized on large cluster architectures with the built-in MPI helper.

The package was first published with @donges_unified_2015 and has since been maintained as an open source project. After more than a decade of consistent feature contributions but fluctuating availability of maintenance resources, we have recently coordinated efforts to enable a series of minor version releases. This publication accompanies pyunicorn's first major version release reflecting pyunicorn's establishment as open source scientific software (cf. [semver.org](https://semver.org)). Pyunicorn v1.0 features a range of additional functionality and a more versatile and robust package.



# Statement of need

Potential research purposes of pyunicorn have been laid out by @donges_unified_2015. The publications referenced in section \ref{research_impact_statement} showcase further applications covering a wide range of disciplines. The need for the pyunicorn package has therefore sufficiently been illustrated. The need for the pyunicorn package has therefore sufficiently been illustrated. The motivation for a follow-up publication of the package at this point in time is twofold. First, pyunicorn proves the value of developing and maintaining a highly specialised code base over a long time. Second, the work that has recently been invested in the project leading to the release of version 1.0 requires an update to the original publication.

Pyunicorn has continuously grown over the years as scientists and other users contributed. With a growing code base and fluctuating levels of funding and expertise available, it has proven challenging to maintain the package to a solid standard over time. Over the last 3 years, we were able to coordinate as a small group combining the needed expertise and working-hours to tackle a significant maintenance backlog. A row of minor version releases have since been issued which contain additional features and worthwhile adaptations.

As sections \ref{software_design} and \ref{research_impact_statement} further set out, pyunicorn is now a more versatile and robust tool than ever. The release of v1.0 reflects the packages established API which has largely remained stable since its first publication. Pyunicorn may further serve as an example for the feasibility of the long-term maintenance of open-source scientific software under the typical fluctuations of available resources.


# State of the field

Pyunicorn, is designed to combine methods from complex network theory and timeseries analysis in a single toolbox and – more importantly – contains further specialised and more uncommon methods that are derived from this synthesis. Many of the derived methods have been established by affiliated research groups themselves. Pyunicorn currently provides their only actively maintained and publicly available implementation.

There is a row of existing Python libraries that cover different aspects of pyunicorn's functionality respectively. [`PyRQA`](https://pypi.org/project/PyRQA/) is a more specialised tool for performing recurrence quantitative analysis that is optimized for handling large datasets [@rawald_pyrqa_2017]. 
@pessa_ordpy_2021 provide a sophisticated package for timeseries analysis with ordinal networks named [`ordpy`](https://pypi.org/project/ordpy/). Users who seek to perform surrogate timeseries generation can resort to the Surrogate Modeling Toolbox [`smt`](https://pypi.org/project/smt/) [@bouhlel_smt_2019]. More recently, the python packages [`irreversibility`](https://pypi.org/project/irreversibility/) (for irreversibility tests of timeseries, cf. @zanin_irreversibility_2025) and [`pynamicalsys`](https://pypi.org/project/pynamicalsys/) (for dynamical systems analysis, cf. @sales_pynamicalsys_2025) have been added to the mix of related software. Moreover, long established Python libraries such as [`networkx`](https://networkx.org) and [`python-igraph`](https://python.igraph.org) extensively cover network and graph calculations.

Yet, pyunicorn has maintained its unique position in bridging the above fields while adding to established packages. For instance, pyunicorn's backbone `Network` class is built around `Graph` objects from `python-igraph` and expands its functionality to more uncommon/specialised variations of network theory such as interacting networks or node-splitting-invariant measures. Yet, the core strength of the package lies in seamlessly integrating network handling with timeseries analysis methods, as in recurrence network analysis or climate networks.

The contained methods have especially been developed and applied in the context of climate and earth system sciences. The generality of the network approach, however, allows for a much wider applicability. A selection of research applications of pyunicorn is described in section \ref{research_impact_statement}.


# Software design
\label{software_design}

Pyunicorn v1.0 continues the original implementation philosophy of the package, which is to provide a common container for conceptually related methods co-developed in affiliated research groups. By adopting a modular class-inheritance structure, the mathematical relationships and historical development of methods are intuitively reflected. A simple example for this intuition is the `RecurrenceNetwork` class, which is a child of the `Network` and `RecurrencePlot` classes (see fig. 2).

![Overview of Pyunicorn's modules and contained classes.](img/module_overview.png)

![Inheritance and composition hierarchies reflecting the mathematical relationships of methods, at the example of the `RecurrenceNetwork` class.](img/class_inheritance.png){width=7cm}

The continuation of these design principles can be illustrated with more recent additions to the package. For example, the `EventSeriesClimateNetwork` inherits from the additional `EventSeries` and the established `ClimateNetwork` classes. Also, the newly added `Cached` class neatly integrates into the object-oriented package structure. As a mix-in class that is built around Python's own caching methods, it adds need-specific memoization to key classes of Pyunicorn. New functionality in the `RecurrenceNetwork` class exemplifies how the package is continuously extended to serve specific research interests: Requested by a doctoral student affiliated with our group (Simon Fahrländer) and after consultation with one of the originators of Recurrence Network theory (Jobst Heitzig), we revised the implementation of node-splitting-invariant shortest-path betweenness to enable its calculation on directed networks in a mathematically sound way. As scientific software ideally does, Pyunicorn can thus not only provide the implementation, but can also act as a catalyst for niche knowledge exchange.

For a full record of additions to the package since its original publication see our [Changelog](https://github.com/pik-copan/pyunicorn/blob/master/CHANGELOG.rst).


# Research impact statement
\label{research_impact_statement}


Pyunicorn has continuously been employed in research since its first publication. Publications that have used pyunicorn at least partly in their analysis are based in or touch upon a range of disciplines: biology, e.g. for statistical tests in cancer research [@amemiya_cancer_2025], EEG data analysis [@frolov_recurrence_2023; @lechner_depressive_2024], neural interactions in cortical networks during decision-making [@maksimenko_neural_2019] and even evolution of mammals [@bekeraite_evolutionary_2025]; astrophysics, e.g. in the analysis of variability of active galactic nuclei [@phillipson_galactic_2023], black holes [@broadbent_cygnus_2023] and stars [@george_betelgeuse_2020]; particle physics [@mullin_susy_2021]; geophysics, e.g. for the exploration of time series in crustal displacements [@hobbs_gnss_2018] and other applications [@talavera_mantle_2023; @donner_magnetosphere_2019]; engineering, e.g. for the detection of thermoacustic instabilities in rocket chambers [@waxenegger_rocket_2021] and other applications [@geier_oscillators_2024]; and for social applications, e.g. for the detection of common features of societal marginalization [@schleussner_minorities_2016]
A main application since first publication have been the climate sciences [@sumit_india_2026; @jiang_tibet_2024; @moinat_tipping_2024; @haas_pitfalls_2023; (@sun_texas_2018); (@li_pakistan_2026); @marwan2021; @caesar_amoc_2020; @franke_anomalies_2017; @franke_holocene_2017; @wolf_baiu_2021; @wolf_itcz_2021; @wolf_connectivity_2021; @donges2015b; @nocke_visual_2015; @wiedermann_hierarchical_2017; @lekscha_windowed_2020], often, for example, for the analysis of El Niño related phenomena [@feng_enso_2017; @oluwole_enso_2017; @broni-bedaiko_enso_2019; @ekhtiari_enso_2021; @wiedermann_enso_2016], as well as general network and non-linearity applications [@silini_entropy_2021; @yuan_correlations_2024; @medrano_radius_2021; @wiedermann_surrogates_2016; @odenweller_paired-event_2020; @sales_stickiness_2023; @subramaniyam_signatures_2015; @lekscha_phasespace_2018; @alberti_magnetic_2020].
Therefore, it is safe to say that pyunicorn has exhibited a high uptake from the community, with 26 of 46 publications coming from authors that have not been affiliated with the pyunicorn team. Additionally, pyunicorn provides educational value with the example notebooks that have been provided since original publication, which can be used to gain understanding methods of time series and complex network analysis for students and practitioners. It consistently has been used in the education of university and doctoral students.



# AI usage disclosure

No generative AI was used in the writing of this manuscript or software. AI coding agents may have occasionally been used for software maintenance or review purposes by pyunicorn contributors and maintainers as available at the time.

# Author contributions

FK has written the manuscript and coordinated software maintenance and release. MB has written the Research Impact Statement. BB, MB, JFD and RVD have reviewed and enhanced the manuscript. BB has provided both hands-on work and expert guidance for software development and maintenance. JFD and RVD have cared for funding and supervised development. FK and JFD have coordinated the manuscript publication.

# Acknowledgements

We acknowledge all code and bug-report contributions to Pyunicorn that have been issued over the years. We are especially thankful for the code and maintenance work provided by Max Bechtold, Ronja Hotz and Jonathan Kroenke. Besides the direct coding work, we would like to thank Pyunicorn's original co-developer Jobst Heitzig for his availability for consultation.

# References