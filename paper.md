---
title: 'decoint: An IEEE 1788.1-2017 Compliant Interval Arithmetic Library for Python Using gmpy2'
tags:
  - Python
  - interval arithmetic
  - validated numerics
  - IEEE 1788
  - gmpy2
authors:
  - name: Arjav Sharma
    orcid: 0009-0001-6347-732X
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: September 2026
bibliography: paper.bib
---

# Summary
`decoint` is a Python library that implements interval arithmetic according to the IEEE 1788.1-2017 standard for Simplified Interval Arithmetic. It was developed to address floating point rounding errors in critical applications. The library provides a framework for executing standard set based interval arithmetic while guaranteeing full containment using directed rounding. To ensure strict containment, `decoint` uses gmpy2 MPFR values to enforce rounding modes. Around 5000 test cases that are pulled from the official ITF1788 repository are used to ensure that the library is fully standards compliant.


The library uses the IEEE 1788 decoration system, containing 5 decorations, to provide metadata to calculations. This system provides useful metadata during calculations to ensure the validity and provide context to the provided result. Essentially, `decoint` provides rigorous error bounding and low level numerical safety to a pure pythonic interface.

# Statement of Need

In scientific computing, IEEE 754 binary64 floating point arithmetic introduces reliability limitations, primarily rounding errors due to the inability to represent fractions whose denominators are not a power of 2. Often, these errors are irrelevant in minor calculations, however they tend to accumulate exponentially over iterative algorithms and matrix operations. This numerical drift can compromise the reliability of scientific computations and safety critical systems, such as Aerospace and Aviation, Control Systems, and Number Theory.

Researchers are often forced to use arithmetic while suffering through floating point error propagation throughout calculations. Interval Arithmetic solves this problem by replacing scalar values with set based calculations. However, basic interval implementations often restrict their evaluation entirely to the lower and upper bounds, neglecting to monitor the underlying domain boundaries and continuity of functions over non-continuous execution spaces.

`decoint` fills this gap within the Python scientific computing community. By wrapping `gmpy2` and executing hardware enforced directed rounding the library ensures that the true results never escape the containment bounds computed. `decoint` also integrates the full IEEE 1788 decoration subsystem. The library prevents silent informational degradation by tracking domain bounds and continuity to track the validity of a result. This gives researchers a standard compliant tool to detect mathematical anomalies, providing numerical rigor directly within Python.

# State of the Field

The level of development of interval arithmetic across different programming languages varies greatly. For example, in the Julia language, `IntervalArithmetic.jl` provides a developed, highly optimized method to perform set based interval computations. However, Python lacks a standards compliant tool to perform interval computations that matches the capabilities of other languages like Julia.

Current Python libraries often fail to meet modern IEEE standards. The legacy package `pyinterval` provide basic interval representations, but is no longer actively maintained, and is not compliant with modern IEEE standards. More recent libraries like `IntvalPy` focus on specialized interval linear systems and classical or Kaucher interval arithmetic, however, they do not implement the complete IEEE 1788.1-2017 decoration system. Without decoration propagation these tools cannot monitor mathematical continuity or domain validity across function evaluations, leading to a lack of metadata to ensure safety across calculations. This leaves Python researchers without an option that delivers both hardware enforced containment and error state tracking. `decoint` directly fills this gap, providing a standard aligned tool to meet the modern demands of computational science.

# Software Architecture and Implementation

The implementation of `decoint` uses a multi-layered object architecture designed to separate low level rounding from core function logic and metadata tracking. The library uses two main classes, the `Interval` class which defines both an infimum and a supremum for the interval, and the `DecoratedInterval` class, which pairs an interval alongside the IEEE 1788 decoration. The library uses standard 64 bit precision.

The pipeline for interval computations flows through a three tier hierarchy:

1. **The Rounding Layer:** Executes directed rounding (e.g., `sin_up`, `sin_down`) by casting inputs to `gmpy2` `mpfr` types within context managers (`with context(get_context(), round=RoundUp/RoundDown)`). This enforces rounding toward $+\infty$ or $-\infty$ during evaluation without modifying the user's global runtime environment.
2. **The Interval Function Wrappers:** Built above the rounding layer, these wrappers handle transformations across non-monotonic functions. When performing the interval computation, the wrapper isolates the critical points, boundaries, and global extrema (maximum and minimum bounds) over the subset which resolves edge cases before returning an `Interval`.
3. **The DecoratedInterval Function Wrapper:** At the highest level, this wrapper intercepts the arithmetic to analyze the function's characteristics over the input domain. By parsing the tracking history for domain violations, mathematical discontinuities, poles, or infinite boundaries, this layer determines and adds the correct decoration, which is then returned to the user as a `DecoratedInterval`.

# Research Impact Statement

`decoint` provides immediate value to researchers by providing reliable guaranteed containment and the elimination of floating point rounding errors, as well as reliable error state tracking. With extensive ITF1788 edge case testing, it provides a reliable tool for verifying numerical stability across scientific computing and research.

To show the viability of the library, `decoint` was used to analyze error growth in the Logistic Map [@sharma2026predictability]. By implementing Mean Value Forms, the library tracks loss of state certainty in chaotic regimes while demonstrating contraction down to machine precision ($\approx 10^{-16}$) in stable regimes.

# AI Usage Disclosure

Generative artificial intelligence tools were utilized during the development of this project for automated code review, debugging assistance, and manuscript copy editing. All core code implementations, mathematical logic, and final manuscript content were comprehensively reviewed, verified, and finalized by the human author to ensure complete accuracy and adherence to standards.

# Acknowledgements

The author acknowledges the IEEE 1788 working group for establishing the foundational software and specifications that enabled this project.

# References
