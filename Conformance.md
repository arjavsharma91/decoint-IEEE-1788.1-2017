# IEEE 1788.1-2017 Conformance Document

This document outlines the architecture, mathematical guarantees, and standard-compliance matrix for this Python interval arithmetic library against the **IEEE 1788.1-2017 Standard for Simplified Interval Arithmetic**.

---

## 1. Architectural Foundations

The library implements a strict decoupling between set boundaries and behavioral metadata through two primary evaluation layers.

### 1.1 The Flavor Layer (`Interval`)
* **Mathematical Set:** Tracks closed connected real intervals $[a, b]$ elements of the set $\mathbb{R} \cup \{-\infty, +\infty\}$ where $a \le b$.
* **Empty Set Representation:** Supported natively. Any configuration resulting in inverted bounds ($a > b$) dynamically normalizes to a canonical `Interval.empty()` state.
* **Directed Rounding Control:** Utilizes strict MPFR core engine settings via `gmpy2` context blocks (`RoundUp`, `RoundDown`). All promotions, boundary transformations, and scalar math happen explicitly inside these blocks to prevent precision leaks from native Python floating-point conversions.

### 1.2 The Metadata Layer (`DecoratedInterval`)
* **Composition:** Encapsulates a bare `Interval` and a strict mathematical `Decoration` enum tracking function continuity and definition states.
* **Lattice Hierarchy:** Fully honors the ordered state transitions defined by the standard:
  $$\text{COM (Comprehensive)} \succ \text{DAC (Defined \& Continuous)} \succ \text{DEF (Defined)} \succ \text{TRV (Trivial)}$$
* **NaI (Not-an-Interval):** Supported via `DecoratedInterval.new_nai()` for uninitialized objects or terminal execution states.

---

## 2. Comprehensive Function & Operation Matrix

All functions exported by the library are structured via strict input coercion (`_coerce()`), explicit NaI or empty-state propagation, and automatic decoration down-leveling based on boundary properties.

### 2.1 Basic Arithmetic & Lattice Operations
| Function | Bare Operational Logic | Decoration Mapping Rule |
| :--- | :--- | :--- |
| `add(x, y)` / `sub(x, y)` | Endpoint math under directed rounding. | `combine(x.dec, y.dec)`. Demotes `COM` $\rightarrow$ `DAC` if result is unbounded. |
| `mul(x, y)` / `div(x, y)` | 4-point evaluations or explicit zero-cross branching. | Drops to `TRV` for division by an interval containing zero. |
| `reciprocal(x)` | Maps $1/x$. Handles split limits at $0$. | Downgrades to `TRV` if domain contains zero. |
| `fma(x, y, z)` | Atomic $x \cdot y + z$ execution inside a single MPFR context sweep. | `combine(x.dec, y.dec, z.dec)`. Demotes to `DAC` if unbounded. |
| `interval_min(x, y)` | Set-theoretic infimum matching `min(x.lo, y.lo)` / `min(x.hi, y.hi)`. | Always forced to `TRV` due to non-continuous derivative boundaries. |
| `interval_max(x, y)` | Set-theoretic supremum matching `max(x.lo, y.lo)` / `max(x.hi, y.hi)`. | Always forced to `TRV` due to non-continuous derivative boundaries. |

### 2.2 Algebraic, Power, and Root Functions
| Function | Bare Operational Logic | Decoration Mapping Rule |
| :--- | :--- | :--- |
| `sqr(x)` | Parabolic transformation; sets lower bound to $0$ if domain crosses $0$. | Preserves decoration; demotes to `DAC` if unbounded. |
| `sqrt(x)` | Evaluates $\sqrt{x}$. Completely negative bounds return `Interval.empty()`. | `new_nai()` if completely negative. Partial negative drops to `TRV`. |
| `nth_root(x, n)` | Strict integer scalar constraint on $n$. Parity-dependent branching (odd vs even). | Preserves incoming decoration; domains restricted on even $n$. |
| `pow_int(x, n)` | Strict integer scalar constraint on $n$. Preserves negative base evaluations. | Parity tracks monotonicity; `COM` $\rightarrow$ `DAC` if unbounded. |
| `pow_interval(x, y)` | General real power $X^Y$. Requires strictly positive base interval ($X > 0$). | `new_nai()` if base $X$ contains negative values. Otherwise standard merge. |

### 2.3 Exponential & Logarithmic Functions
| Function | Bare Operational Logic | Decoration Mapping Rule |
| :--- | :--- | :--- |
| `exp(x)` / `exp2(x)` / `exp10(x)` | Strict monotonic increasing mapping across the entire real line. | `COM` across domains; demotes to `DAC` if bounds hit $+\infty$ or $-\infty$. |
| `log(x)` / `log2(x)` / `log10(x)` | Complete out-of-domain ($X.hi \le 0$) returns `Interval.empty()`. | Completely out-of-domain maps to `TRV`. Partially out-of-domain drops to `TRV`. |

### 2.4 Trigonometric Functions
| Function | Bare Operational Logic | Decoration Mapping Rule |
| :--- | :--- | :--- |
| `sin(x)` / `cos(x)` | Periodicity analysis tracking local turning points ($[-1, 1]$ clamping). | Always bounded; preserves `COM` status across full domains. |
| `tan(x)` | Periodic asymptotes checked. Ranges hitting singularity expand to $[-\infty, +\infty]$. | Demotes to `TRV` if domain contains an odd multiple of $\pi/2$. |
| `asin(x)` / `acos(x)` | Restricted domain mapping on $[-1, 1]$. Values completely outside return `empty()`. | Fully out-of-domain returns `TRV`. Partially out-of-domain drops to `TRV`. |
| `atan(x)` | Continuous mapping tracking bounded outputs asymptotic to $\pm\pi/2$. | Bounded output; maps to `COM`. |
| `atan2(y, x)` | Four-quadrant inverse tangent tracking coordinate space signs. | Drops to `TRV` if domain crosses origin singularities. |

### 2.5 Hyperbolic & Special Functions
| Function | Bare Operational Logic | Decoration Mapping Rule |
| :--- | :--- | :--- |
| `sinh(x)` / `tanh(x)` | Monotonic increasing continuous mappings across the entire real line. | `COM`; downlevels to `DAC` if unbounded. |
| `cosh(x)` | Bounded below by $1.0$. Turning point checks around $0$. | `COM`; downlevels to `DAC` if unbounded. |
| `asinh(x)` / `atanh(x)` | Continuous tracking of inverse operations. `atanh` restricted to $(-1, 1)$. | Partial domain crossings drop to `TRV`. |
| `acosh(x)` | Domain restricted to $[1, +\infty)$. | Partial domain crossings drop to `TRV`. |
| `abs(x)` | Standard magnitude extraction. Non-negative output clamping. | Always forced to `TRV` due to the non-differentiable cusp at $0$. |
| `sign(x)` | Signum mapping returning discrete step choices $\{-1, 0, 1\}$. | Strictly drops to `TRV` across step transitions. |

---

## 3. Strict Verification & Integrity Guarantees

1. **Containment Invariant:** No underlying scalar operation relies on native operators without validation. Directed rounding modes are enforced natively at the MPFR layer before an operation executes.
2. **Double-Rounding Eradication:** Functions like `pow_interval` utilize native multi-precision library entries rather than sequence composition to maintain exact single-step bit rounding integrity.
3. **Exception Freedom:** Out-of-domain evaluations avoid standard Python runtime crashes, instead channeling safely into mathematically exact `Interval.empty()` or state-managed `new_nai()` configurations.
