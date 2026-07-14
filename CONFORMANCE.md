# IEEE 1788.1-2017 Conformance Statement
**Library:** decoint   
**Version:** 1.0.0  
**Author:** Arjav Sharma   
**Date:** July 5, 2026  

---

## 1. Underlying Numeric Type

This library achieves strict IEEE 1788.1-2017 compliance by anchoring all endpoint calculations to arbitrary-precision floating-point numbers via the `gmpy2` library, which wraps the GNU MPFR C engine. Instead of relying on native Python `float` types (which map to hardware-dependent IEEE 754 binary64 and risk implicit precision leaks), all numeric constants, strings, and inputs are explicitly promoted to MPFR instances using a centralized factory layer (`Number`). This configuration ensures that every upper and lower bound modification is strictly bound to the active MPFR hardware context flags. Directed rounding modes (`RoundUp` and `RoundDown`) are dynamically set within localized atomic execution blocks (`with context(...)`). This approach eliminates double-rounding issues during complex transcendental operations and guarantees a watertight containment enclosure. Exponent minimums and maximums are manually set to ensure compliance with IEEE 754 Floating Point Numbers.

---

## 2. Supported Operations Checklist

The following table itemizes the operations and elementary functions implemented by the library, confirming their adherence to the set-theoretic and decoration rules of the standard:

| Operation Type | Supported Functions | Conformance Status |
| :--- | :--- | :--- |
| **Basic Arithmetic** | `add`, `sub`, `mul`, `div`, `reciprocal`, `fma` | Fully Compliant |
| **Lattice / Set Ops** | `interval_min`, `interval_max` | Fully Compliant |
| **Algebraic / Powers**| `sqr`, `sqrt`, `pow_int`, `nth_root`, `pow_interval` | Fully Compliant |
| **Exponentials / Logs**| `exp`, `exp2`, `exp10`, `log`, `log2`, `log10`, `sqr` | Fully Compliant |
| **Trigonometric** | `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2` | Fully Compliant |
| **Hyperbolic** | `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh` | Fully Compliant |
| **Special Primitive** | `abs`, `sign`, `interval_trunc`, `interval_floor`, `interval_ceil` | Fully Compliant |
| **Set Operations** | `hull`, `intersection` | Fully Compliant |

---

## 3. Exception Handling & Interval Decorations

* **Exception-Free Execution:** In compliance with the standard, structural failures of the library safely propagate to an NAI state rather than throwing a runtime error.
* **Lattice Decoration Tracking:** The library tracks continuous metadata updates across the standard's ordinal decoration hierarchy (`COM` $\succ$ `DAC` $\succ$ `DEF` $\succ$ `TRV` $\succ$ `ILL`). Incoming decorations are systematically merged using a `combine()` function that extracts the weakest common state.
