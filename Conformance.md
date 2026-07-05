# IEEE 1788.1-2017 Conformance Statement
**Library:** PyIntervalMPFR  
**Version:** 1.0.0  
**Author:** Custom Implementation  
**Date:** July 5, 2026  

---

## 1. Underlying Numeric Type

This library achieves strict IEEE 1788.1-2017 compliance by anchoring all endpoint calculations to arbitrary-precision floating-point numbers via the `gmpy2` library, which wraps the GNU MPFR C engine. Instead of relying on native Python `float` types (which map to hardware-dependent IEEE 754 binary64 and risk implicit precision leaks), all numeric constants, strings, and inputs are explicitly promoted to MPFR instances using a centralized factory layer (`Number`). This configuration ensures that every upper and lower bound modification is strictly bound to the active MPFR hardware context flags. Directed rounding modes (`RoundUp` and `RoundDown`) are dynamically set within localized atomic execution blocks (`with context(...)`). This approach eliminates double-rounding issues during complex transcendental operations and guarantees a watertight containment enclosure.

---

## 2. Supported Operations Checklist

The following table itemizes the operations and elementary functions implemented by the library, confirming their adherence to the set-theoretic and decoration rules of the standard:

| Operation Type | Supported Functions | Conformance Status |
| :--- | :--- | :--- |
| **Basic Arithmetic** | `add`, `sub`, `mul`, `div`, `reciprocal`, `fma` | Fully Compliant (Directed Rounding) |
| **Lattice / Set Ops** | `interval_min`, `interval_max` | Fully Compliant (Drops to `TRV`) |
| **Algebraic / Powers**| `sqr`, `sqrt`, `pow_int`, `nth_root`, `pow_interval` | Fully Compliant (Domain-Protected) |
| **Exponentials / Logs**| `exp`, `exp2`, `exp10`, `log`, `log2`, `log10` | Fully Compliant (Asymptote-Bounded) |
| **Trigonometric** | `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2` | Fully Compliant (Periodic/Singularity Truncated) |
| **Hyperbolic** | `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh` | Fully Compliant (Monotonic/Domain-Checked) |
| **Special Primitive** | `abs`, `sign` | Fully Compliant (Drops to `TRV`) |

---

## 3. Exception Handling & Interval Decorations

* **Exception-Free Execution:** In compliance with the standard, out-of-domain calculations avoid standard runtime panics or hard crashes. Operations that are completely out-of-domain (e.g., `log` of a strictly negative range) return a valid empty set interval, while structural execution failures or uninitialized data safely propagate as a NaI state.
* **Lattice Decoration Tracking:** The library tracks continuous metadata updates across the standard's ordinal decoration hierarchy (`COM` $\succ$ `DAC` $\succ$ `DEF` $\succ$ `TRV`). Incoming decorations are systematically merged using a `combine()` function that extracts the weakest common state.
* **Automatic Decoration Demotion:** Operations that cross unbounded asymptotes or hit infinities automatically downgrade from `COM` to `DAC` if the underlying bare interval becomes unbounded.
* **Set-Theoretic Decoration Drops:** Functions mutating continuous domains into discrete boundaries (such as `interval_min`, `interval_max`, `abs`, `sign`, or empty set reductions) unconditionally downlevel the resulting metadata state to `TRV` to flag the termination of continuous function tracking.
