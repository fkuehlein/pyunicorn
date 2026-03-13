---
title: 'Pyunicorn 1.0'
tags:
  - Python
  - complex systems
  - networks
  - timeseries analysis
authors:
  - given-names: Fritz
    surname: Kühlein
    orcid: 0000-0000-0000-0000
    corresponding: true
    affiliation: "1"
  - given-names: Boyan
    surname: Beronov
    affiliation: "1, 2"
  - given-names: Reik V.
    surname: Donner
    affiliation: "1, 3"
  - given-names: Jonathan F.
    surname: Donges
    affiliation: "1, 4"
affiliations:
 - name: Potsdam Institute for Climate Impact Research (PIK), Germany
   index: 1
 - name: Boyan's Affiliation (if sensible), Canada
   index: 2
 - name: Magbeburg-Stendal University of Applied Sciences, Germany
   index: 3
 - name: Stockholm Resilience Center, Sweden
   index: 4
date: 1 April 2026
bibliography: paper.bib
---

# Summary

*Prompt: A description of the high-level functionality and purpose of the software for a diverse, non-specialist audience.*

Pyunicorn is a toolbox for complex systems analysis that is written in Python and C. Pyunicorn contains implementations of highly specialised methods that derive from the synthesis of network theory and timeseries analysis, but can also serve as a general-purpose tool for complex networks. Pyunicorn is fast, as computationally expensive functions are written in C, or precompiled via Cython. It can easily be parallelized on large cluster architectures with the built-in MPI helper.

The package was first published with @donges_unified_2015 and has been maintained as an open source project since. The library has continuously grown over the years as scientists and other users took the chance to contribute. These contributions have originated both from within and outside the direct proximity of the initial developers. Maintenance work on the project was largely provided by young researchers, usually master students supervised by J. Donges, B. Beronov and R. Donner.

With a growing codebase and fluctuating levels of funding and expertise available, it has proven difficult to keep up the maintenance to a solid standard over time. Therefore by 2023, a significant maintenance backlog had accumulated despite the efforts of a row of dedicated maintainers.

Over the last 3 years, we were able to coordinate as a small group to combine the needed expertise and working-hours and tackle a great chunk of overdue maintenance. We have thereby put Pyunicorn back on track and available for its userbase. A couple of extra features and timely adaptations have further been issued.

This process can serve as a working example of keeping highly specialised scientific software alive over a timeframe that is quite long relative to typical innovation-rates in computational soft- and hardware. Pyunicorn is good proof of the feasability of such a project under the given resource limitations.

More importantly though, after over 10 years of gradual development Pyunicorn is now a more versatile and robust tool than ever and therefore deserves the attention of this re-issue. 


# Statement of need

*Prompt: A section that clearly illustrates the research purpose of the software and places it in the context of related work. This should clearly state what problems the software is designed to solve, who the target audience is, and its relation to other work.*

Potential research purposes of Pyunicorn have extensively been laid out in @donges_unified_2015. The publications in \ref{research_impact_statement} showcase further interesting applications.

More than 10 years of development have proven Pyunicorn to be worth keeping alive, as new and unforeseen applications and enhancements continue to come about. (Blabla sentence I know)

With this in mind, the question of need is therefore sensibly pointed not to the package per-se, but to the re-issue at this point in time. *And to Version 1.0?*

There are two key motivations for this. Firstly, Pyunicorn proves that it makes sense to keep a highly specialised, although "legacy" codebase alive and maintained over a long time. Secondly, Pyunicorn is now versatile and packed as ever and deserves an update to its original publication.


# State of the field

*Prompt: A description of how this software compares to other commonly-used packages in the research area. If related tools exist, provide a clear “build vs. contribute” justification explaining your unique scholarly contribution and why existing alternatives are insufficient.*

Pyunicorn, is designed to unify methods from complex network theory and timeseries analysis under a single hood and – more importantly – deriving further specialised and more uncommon methods from this synthesis. Many of these derived methods have been established by affiliated research groups themselves and Pyunicorn currently provides their only actively maintained and publicly available implementation.

A row of Python libraries cover different aspects of Pyunicorn's functionality respectively. [`PyRQA`](https://pypi.org/project/PyRQA/) is a more recently published tool for performing recurrence quantitative analysis on large datasets in a computationally efficient way [@rawald_pyrqa_2017]. Users who seek to perform surrogate timeseries generation can resort to the Surrogate Modeling Toolbox [`smt`](https://pypi.org/project/smt/). Moreover, long established Python libraries such as [`networkx`](https://networkx.org) and [`python-igraph`](https://python.igraph.org) extensively cover network and graph calculations.

Yet, over 10 years after its first publication, Pyunicorn currently still finds itself in the unique position to feature functionality that bridges many of these fields and adds to established packages. In fact, Pyunicorn's backbone `Network` class is built around `Graph` objects from `python-igraph`. Yet, it expands its functionality to variations of network theory such as Interacting Networks, node-splitting-invariant measures, etc. *(to be improved)*.

The contained methods have especially been developed and applied in the context of climate and earth system sciences. The generality of the network approach, however, allows for a much wider applicability.

With new scientific software being published more and more frequently, we aim to put some counterweight on the maintenance of legacy code. Pyunicorn features specialised methods that are far from exploited and as valuable as ever.

A selection of research applications of Pyunicorn is described in \ref{research_impact_statement}.


# Software design

*Prompt: An explanation of the trade-offs you weighed, the design/architecture you chose, and why it matters for your research application. This should demonstrate meaningful design thinking beyond a superficial code structure description.*

Pyunicorn 1.0 continues the original implementation philosophy of the package, which is to provide a common container for conceptually related methods co-developed in affiliated research groups. ~~Pyunicorn integrates these methods in a common format and keep them available for future research.~~ By adopting a  modular class-inheritance structure, the mathematical relationships of methods are intuitively reflected.

This intuition is, for example, realised in the `RecurrenceNetwork` class, which is a child of the `Network` and `RecurrencePlot` classes (see fig. 2): The class structure reflects the "mathematical definition and historical development of recurrence network analysis" [@donges_unified_2015].

![Pyunicorn currently contains 6 modules.](img/module_overview.png)

![Inheritance and composition hierarchies reflect the mathematical relationships of methods.](img/class_inheritance.png)

The package structure is thoroughly described in @donges_unified_2015 and in the package documentation.

The continuation of the above described design principles can be illustrated with more recent additions to the package. For example, the `EventSeriesClimateNetwork` inherits from the additional `EventSeries` and the established `ClimateNetwork` classes. Also, the newly added `Cached` class neatly integrates into the object oriented package design. It acts as an abstract base class to add advanced memoization functionality to key classes of Pyunicorn. Additional functionality in the `RecurrenceNetwork` class exemplifies how the package is continuously extended to serve specific research interests: Requested by a young researcher affiliated with our group (Simon Fahrländer) and after consultation with one of the originators of Recurrence Network theory (Jobst Heitzig), we revised the implementation of node-splitting-invariant shortest-path betweenness to enable its calculation on directed networks in a mathematically sound way. Pyunicorn not only provides the implementation of these specialised methods, but also acts as a catalyst for exchange of knowledge on the underlying theory.

For a full record of additions to the package since its original publication see our [Changelog](https://github.com/pik-copan/pyunicorn/blob/master/CHANGELOG.rst).


- Recent additions:
  - CI with support for linux and windows systems
  - additional classes
    - SpatialNetwork
    - EventSeries, EventSeriesClimateNetwork
    - Cached: overhauled caching
  - additional or revised functionality in classes
    - Network: weighted betweenness measures
    - MapPlot: simplify with cartopy
    - Surrogates: refactor API for OO conformity
    - RecurrencePlot, CoupledClimateNetwork, InteractingNetworks: added functionality by jkroenke


# Research impact statement
\label{research_impact_statement}

*Prompt: Evidence of realized impact (publications, external use, integrations) or credible near-term significance (benchmarks, reproducible materials, community-readiness signals). The evidence should be compelling and specific, not aspirational.*

Pyunicorn has been applied in a row of published analysis right after its first publication.

Recently, it has been applied in my Master's thesis and almost put into TOAD.


# Conclusion

*Optional, might want to add*


# AI usage disclosure

*Prompt: Transparent disclosure of any use of generative AI in the software creation, documentation, or paper authoring. If no AI tools were used, state this explicitly. If AI tools were used, describe how they were used and how the quality and correctness of AI-generated content was verified.*

No AI tools were used in the writing of this paper. AI coding agents might have been used by Pyunicorn contributors as available at the time. AI coding agents have occasionally been used for software maintenance.


# Acknowledgements

*Section added by myself*

We would like to express gratitude to all those who have contributed to Pyunicorn over the years. This especially includes code and maintenance contributions from Max Bechtold, Ronja Hotz, ...
What's more, 