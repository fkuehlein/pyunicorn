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

Two key arguments for this (follow-up) publication:
1. pyunicorn is now versatile and packed as ever and deserves an up-to-date publication
2. it makes sense to keep highly specialised, although "legacy" code alive and maintained over time

---

Pyunicorn is a toolbox for complex systems analysis that is written in Python and C.

It was first published with @donges_unified_2015 and has been maintained as an open source project since. The library has continuously grown over the years as scientists and users took the chance to contribute. These contributions have originated both from within and outside the direct proximity of the initial developers. The project has been maintained by young researchers, most of which master students supervised by J. Donges, B. Beronov and R. Donner.

With a growing codebase and fluctuating levels of funding and expertise available, it has proven difficult to keep up the maintenance to a solid standard over time. Therefore by 2023, a significant maintenance backlog had accumulated despite the efforts of a row of dedicated maintainers.

Over the last 3 years, we were able to coordinate as a small group to combine the needed expertise and working-hours and tackle a great chunk of overdue maintenance. We thereby put Pyunicorn back on track and available for its userbase. A couple of extra features and timely adaptations have further been issued.

This process can serve as a working example of maintaining highly specialised scientific software over a timeframe that is quite long relative to typical innovation-rates in soft- and hardware - and prove its feasability under the given resource limitations.

More importantly though, Pyunicorn is now a more versatile and robust tool than ever and therefore deserves 'a follow-up publication'. 


# Statement of need

*Prompt: A section that clearly illustrates the research purpose of the software and places it in the context of related work. This should clearly state what problems the software is designed to solve, who the target audience is, and its relation to other work.*


Research purpose: See Pyunicorn paper


What problems is it designed to solve?


Who is the target audience?


Therefore: *Need* to maintain such software over a long time, with minimal resources. 


# State of the field

*Prompt: A description of how this software compares to other commonly-used packages in the research area. If related tools exist, provide a clear “build vs. contribute” justification explaining your unique scholarly contribution and why existing alternatives are insufficient.*

There are a row of Python libraries that cover network and graph (networkx, igraph) calculations as well as timeseries analysis, Recurrence Analysis, Eventseries Analysis (?) and such. 

Pyunicorn, is unique in *uni*fying these methods under a single hood and – more importantly – deriving further methods from this What's more, it contains methods that go beyond that and that result from this very unification.

Some of these more uncommon methods have been developed by our original contributors themselves and their implementation is currently only available in Pyunicorn. 

> "While pyunicorn’s development has mostly accompanied advances in climatology and paleoclimatology, the generality of the network approach and its implementation of extensions to standard complex networks like spatio-temporal networks, node weighted measures, coupled functional networks and recurrence networks render the software widely applicable in numerous fields, e.g. medicine, neuroscience, sociology, economics and finance."

The contained methods have especially been developed and applied in the context of climate and earth system sciences. Yet, due to the generality of the network approach, they are more widely applicable.

With new scientific software being published more and more frequently, we aim to put some counterweight on the maintenance of legacy code. Pyunicorn features specialised methods that are far from exploited and as valuable as ever.


# Software design

*Prompt: An explanation of the trade-offs you weighed, the design/architecture you chose, and why it matters for your research application. This should demonstrate meaningful design thinking beyond a superficial code structure description.*

> "pyunicorn is intended as an integrated container for a host of conceptionally related methods which have been developed and applied by the involved research groups for many years." @donges_unified_2015

Pyunicorn 1.0 continues the original implementation philosophy of the package, which is to provide a container for conceptually related methods that derive from the synthesis of complex network and timeseries analysis.

> "inheritance and composition hierarchy reflects the relationships between the analysis methods in use"

Its modular inheritance structure aims to intuitively reflect its mathematical grounding.

This intuition is, for example, realised/manifested in the `RecurrenceNetwork` class, which is a child of the `Network` and `RecurrencePlot` classes: The class structure reflects the "mathematical definition and historical development of recurrence network analysis". (add figure from paper?)

Code structure description to exemplify:

Pyunicorn currently contains 6 modules: (add small table)
- core
- climate
- timeseries
- eventseries
- funcnet
- utils

~~The `core` module contains the backbone `Network` class and further base classes of the library. The `climate` module contains the `ClimateNetwork` and subclasses, as well as an additional class to plot maps using `cartopy`.~~

The class structure is thoroughly described in @donges_unified_2015 as well as the package documentation.

- Recent additions:
  - CI with support for windows and linux systems
  - plotting maps with cartopy
  - overhauled caching


# Research impact statement

*Prompt: Evidence of realized impact (publications, external use, integrations) or credible near-term significance (benchmarks, reproducible materials, community-readiness signals). The evidence should be compelling and specific, not aspirational.*

Pyunicorn has been applied in a row of published analysis right after its first publication.

Recently, it has been applied in my Master's thesis and almost put into TOAD.


# AI usage disclosure

*Prompt: Transparent disclosure of any use of generative AI in the software creation, documentation, or paper authoring. If no AI tools were used, state this explicitly. If AI tools were used, describe how they were used and how the quality and correctness of AI-generated content was verified.*

No AI tools were used in the writing of this paper. AI coding agents might have been used by Pyunicorn contributors as available at the time. AI coding agents have occasionally been used for software maintenance.


# Acknowledgements

*Section added by myself*

We would like to express gratitude to all those who have contributed to Pyunicorn over the years. This especially includes code and maintenance contributions from Max Bechtold, Ronja Hotz, ...
What's more, 