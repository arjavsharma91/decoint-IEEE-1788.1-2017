# Usage Guide: Handling Precision and Numeric Inputs

To ensure the mathematical rigor and strict standard compliance of `decoint`, it is critical to understand how Python handles numeric types before they are passed into the interval engine.

## 1. The String Input Recommendation

When defining intervals with decimal values, **it is highly recommended to pass values as strings rather than standard Python floats.**

```python
from decoint import Interval

# ❌ NOT RECOMMENDED: The floats 1.1 and 2.1 are already imprecise before creating the interval
invalid = Interval(1.1, 2.1)

# ✅ RECOMMENDED: High-precision parsing preserves exact decimal intent
valid = Interval("1.1", "2.1")
```

### Why This Matters

Because `decoint` is built on top of `gmpy2` (leveraging the arbitrary-precision MPFR library), it is capable of tracking exact mathematical boundaries using directed rounding modes. However, if you pass a standard Python float like `1.1`, the precision loss occurs before your library ever sees the data:

1. **Immediate Base-2 Approximation:** Python immediately converts the literal `1.1` into a standard `binary64` hardware float. Because 1.1 cannot be exactly represented in binary, it becomes `1.10000000000000008881784...`.
2. **Imprecise Bounding:** `gmpy2` reads that already-imprecise float, causing the interval bounds to tightly wrap around a corrupted value rather than the exact fractional value of 11/10.

By passing a string representation (`"1.1"`), `gmpy2` parses the exact decimal characters directly into arbitrary precision, allowing `decoint` to apply strict IEEE 1788.1-2017 directed rounding rules (rounding downward for the lower bound and upward for the upper bound) from the true intended value.

### When are Raw Numbers Safe?

You can safely pass raw integers or fractions that have exact binary representations:

```python
# Safe: Integers have exact representations
int_interval = Interval(5, 7)

# Safe: Powers of 2 (e.g., 0.5 = 1/2) have exact binary representations
float_exact = Interval(0.5, 0.5)
```

For any other decimal values, always default to string literals to maintain the mathematical integrity of your interval simulations.

---

## 2. Basic `Interval` Initialization

 A standard interval represents a closed, connected set of real numbers [a, b]. You can define them by passing the lower and upper bounds independently.

```python
from decoint import Interval

# Initialize using exact decimal string literals (Highly Recommended)
a = Interval("-1.5", "2.3")

# Initialize using exact integers or binary-exact floats
b = Interval(1, 5)          # [1, 5]
c = Interval(0.5, 0.5)         # A point interval: [0.5, 0.5]
```

---

## 3. Parsing Interval Strings and Uncertainty Formats

`decoint` can also instantiate intervals directly from a single string representation. This is highly useful when parsing data from experimental logs, configuration files, or user inputs.

### Bound-Style Strings
You can pass a single string enclosed in brackets that defines both the lower and upper bounds explicitly:

```python
# Parse standard bracket notation
val = Interval("[2.1, 3.1]")  # Evaluates to an interval from 2.1 to 3.1
```

### Custom Uncertainty / Error-Margin Formats
In scientific workflows, asymmetric or directional experimental tolerances are common. `decoint` natively parses a strict, character-separated uncertainty syntax directly into exact mathematical intervals. 

The notation follows this exact structure:  
`[Sign][Integer Part].[Fractional Part]?[Uncertainty Value][Direction Token][Exponent Token]`

* **`[Sign]` (Optional):** Explicit positive (`+`) or negative (`-`) indicator for the nominal value.
* **`[Integer Part].[Fractional Part]` (Mandatory):** The nominal value written as a standard decimal number.
* **`?` (Mandatory Separator):** Flags the transition from the nominal value to the uncertainty parameters.
* **`[Uncertainty Value]` (Optional):** An integer that aligns directly with the least significant digit (the very last digit) of the fractional part to define the magnitude of the error.
* **`[Direction Token]` (Optional):** A single character defining the one-sided boundary:
  * `u` (Up): The nominal value is the absolute floor. True value is in the range [Nominal, Nominal + Uncertainty].
  * `d` (Down): The nominal value is the absolute ceiling. True value is in the range [Nominal - Uncertainty, Nominal].
* **`[Exponent Token]` (Optional):** Expressed as `e` or `E` followed by an integer, representing a scientific notation multiplier (10^exponent).

```python
# Upward uncertainty: Base 1.23, error magnitude 4 at the hundredths place (+0.04)
# Evaluates to bound: [1.23, 1.27]
experiment_up = Interval("1.23?4u")

# Downward uncertainty with exponents: Base -0.005, error magnitude 2 at the thousandths place (-0.002), scaled by 10^3
# Evaluates to bound: [-7.0, -5.0]
experiment_scaled = Interval("-0.005?2de3")
```

---

## 4. `DecoratedInterval` Initialization

Decorated intervals pair an existing mathematical `Interval` object with a **decoration** (or flavor). Decorations provide metadata about the evaluation history of the interval (e.g., whether a function evaluation remained continuous across the domain, or if an out-of-bounds operation occurred).

Unlike standard intervals, a `DecoratedInterval` is instantiated by passing an actual **`Interval` instance** along with its tracking state, rather than raw numbers.

The standard IEEE 1788.1-2017 decoration states (ordered from highest validity to lowest) are:
* `com` (Comly): Entirely continuous, bounded, and well-defined.
* `dac` (Defined and Continuous): Bounded and continuous, but may have hit a domain boundary.
* `def` (Defined): Well-defined, but continuity may have been violated.
* `trv` (Trivial): No information or constraints guaranteed (the ultimate fallback/error state).
* `ill` (Ill-Defined): Characterizes an ill-defined or invalid mathematical state or operation context.

```python
from decoint import Interval, DecoratedInterval, Decoration

# 1. Instantiate the underlying mathematical interval
base_interval = Interval("[2.1, 3.1]")

# 2. Wrap it in a DecoratedInterval alongside its decoration state (defaults to Decoration.COM)
di1 = DecoratedInterval(base_interval) 

# Explicitly defining a decorated interval with a specific compliance status
di2 = DecoratedInterval(base_interval, decoration=Decoration.DAC)
```

If an evaluation failure, syntax error, or a similar exceptional issue occurs during execution, the resulting interval will automatically drop to an `NAI` (Not an Interval) state.

---

## 5. Operation Syntax

`decoint` supports standard, intuitive Python arithmetic operators for both `Interval` and `DecoratedInterval` instances. Basic operations like addition, subtraction, multiplication, and division do not require calling verbose internal methods; they map directly to Python's built-in magic methods.

### Supported Arithmetic Operators
* **Addition:** `+`
* **Subtraction:** `-`
* **Multiplication:** `*`
* **Division:** `/`

```python
from decoint import Interval, DecoratedInterval

# Standard Interval Arithmetic
i1 = Interval(1, 2)
i2 = Interval(3, 4)

# Operations can be performed using regular operators
add_res = i1 + i2  # Evaluates to [4, 6]
sub_res = i1 - i2  # Evaluates to [-3, -1]
mul_res = i1 * i2  # Evaluates to [3, 8]
div_res = i1 / i2  # Evaluates to [0.25, 0.66666...]

# Arithmetic also works with mixed valid types (like raw integers)
scale_res = i1 * 5  # Evaluates to [5, 10]

# Decorated Interval Arithmetic
# Tracking rules and decorations propagate through the operators automatically
di1 = DecoratedInterval(Interval("1.0", "2.0"))
di2 = DecoratedInterval(Interval("3.0", "4.0"))

decorated_add = di1 + di2
```

---

## 6. Algebraic and Power Operations

`decoint` provides specialized functions for executing algebraic powers, squares, and roots rigorously. These functions ensure that the interval bounds are mapped correctly according to properties like function parity and monotonicity.

Depending on the operation, the syntax accepts a single interval, an interval paired with an integer, or two separate intervals.

### Unary Operators
These functions take a single `Interval` or `DecoratedInterval` as their sole argument.

```python
from decoint import Interval, sqr, sqrt

# Square an interval
# Evaluates to [1, 4]
res_sqr = sqr(Interval(1, 2))

# Square root of an interval
# Evaluates to [2, 3]
res_sqrt = sqrt(Interval(4, 9))
```

### Interval and Integer Operators
These functions require an `Interval` or `DecoratedInterval` for the base/radicand, and an integer for the exponent or root degree.

```python
from decoint import Interval, pow_int, nth_root

# Raise an interval to an integer power
# Evaluates to [8, 27]
res_pow_int = pow_int(Interval(2, 3), 3)

# Take the nth root of an interval using an integer degree
# Evaluates to [2, 3]
res_nth_root = nth_root(Interval(4, 9), 2)
```

### Interval and Interval Power Operators
For operations where both the base and the exponent are uncertain, use interval-to-interval power functions.

```python
from decoint import Interval, pow_interval

# Raise an interval base to an interval exponent
res_pow_intv = pow_interval(Interval(1, 2), Interval(3, 4))
```

---

## 7. Exponential and Logarithmic Operations

`decoint` offers robust tracking for standard transcendental functions. Because all exponential and logarithmic functions are strictly monotonic, the mathematical bounds map directly without complex internal branching. 

All functions listed below are **unary operators** and accept either an `Interval` or `DecoratedInterval` as their single argument. For log functions, omitting a numeric suffix defaults safely to the natural logarithm (base e).

### Supported Transcendental Operators
* **Exponentials:** `exp` (base e), `exp2` (base 2), and `exp10` (base 10)
* **Logarithms:** `log` (natural log, base e), `log2` (base 2), and `log10` (base 10)

```python
from decoint import Interval, exp, exp2, exp10, log, log2, log10

# Exponential Operations
e_power   = exp(Interval(1, 2))     # Base e exponential
two_power = exp2(Interval(1, 2))    # Base 2 exponential -> [2.0, 4.0]
ten_power = exp10(Interval(1, 2))   # Base 10 exponential -> [10.0, 100.0]

# Logarithmic Operations
nat_log   = log(Interval(1, 2))     # Natural logarithm (base e)
base2_log = log2(Interval(2, 4))    # Base 2 logarithm -> [1.0, 2.0]
base10_log= log10(Interval(10, 100))# Base 10 logarithm -> [1.0, 2.0]
```

---

## 8. Trigonometric Operations

Trigonometric mappings require careful boundary calculations due to periodic extrema (like the peaks and troughs of sine and cosine) and asymptotic domain gaps (like the poles of tangent). `decoint` natively accounts for these internal critical points, ensuring outer-bound preservation across complete intervals.

With the exception of the binary `atan2` operator, all trigonometric methods are **unary operators** accepting a single `Interval` or `DecoratedInterval`.

### Supported Trigonometric Functions
* **Standard Trig:** `sin`, `cos`, `tan`
* **Inverse Trig:** `asin`, `acos`, `atan`
* **Binary Inverse Tangent:** `atan2`

```python
from decoint import Interval, sin, cos, tan, asin, acos, atan, atan2

# Standard Trigonometric Functions (Arguments in Radians)
# Handles internal extrema safely (e.g., crossing pi/2 wraps perfectly to 1.0)
sin_res = sin(Interval(0, 2))
cos_res = cos(Interval(0, 3.14159))
tan_res = tan(Interval("-1.0", "1.0"))

# Inverse Trigonometric Functions
asin_res = asin(Interval("-0.5", "0.5"))
acos_res = acos(Interval(0, 1))
atan_res = atan(Interval(-1, 1))

# Binary Inverse Tangent (atan2)
# Accepts two intervals representing the y and x coordinates respectively
atan2_res = atan2(Interval(1, 2), Interval(3, 4))
```

---

## 9. Hyperbolic Operations

`decoint` natively tracks hyperbolic functions and their inverses. While functions like `sinh`, `tanh`, `asinh`, `acosh`, and `atanh` are strictly monotonic over their domains, the `cosh` function includes a global minimum at $x = 0$. The engine safely registers this critical inflection point to produce rigorous outer boundaries.

All listed functions are **unary operators** and take an `Interval` or `DecoratedInterval` instance as their lone argument.

### Supported Hyperbolic Functions
* **Standard Hyperbolics:** `sinh`, `cosh`, `tanh`
* **Inverse Hyperbolics:** `asinh`, `acosh`, `atanh`

```python
from decoint import Interval, sinh, cosh, tanh, asinh, acosh, atanh

# Standard Hyperbolic Functions
# cosh evaluates across 0 tracking the lower bound boundary correctly at 1.0
sinh_res = sinh(Interval(-1, 1))
cosh_res = cosh(Interval(-1, 1))  
tanh_res = tanh(Interval(-2, 2))

# Inverse Hyperbolic Functions
asinh_res = asinh(Interval(-5, 5))
acosh_res = acosh(Interval(1, 5))    # Domain restricted to [1, inf)
atanh_res = atanh(Interval("-0.5", "0.5")) # Domain restricted to (-1, 1)
```

---

## 10. Special Primitives

`decoint` provides structural primitives for absolute scaling, sign determination, and interval boundary truncation. These primitives ensure that discrete and non-continuous transformations (like floor or ceiling limits) preserve set boundaries correctly according to standard interval arithmetic logic.

All primitive functions in this section are **unary operators** that accept a single `Interval` or `DecoratedInterval` instance.

### Supported Special Primitives
* **Magnitude and Sign:** `abs`, `sign`
* **Discrete Rounding:** `interval_trunc`, `interval_floor`, `interval_ceil`

```python
from decoint import Interval, abs, sign, interval_trunc, interval_floor, interval_ceil

# Absolute Value and Sign Determination
# abs handles intervals containing zero by fixing the lower bound to 0
abs_res  = abs(Interval(-2, 3))               # Evaluates to [0, 3]
sign_res = sign(Interval(-5, 2))              # Evaluates to [-1, 1]

# Discrete Rounding Primitives
# These map intervals cleanly onto integer-bounded sets
trunc_res = interval_trunc(Interval("-1.7", "2.3")) # Truncates toward zero -> [-1, 2]
floor_res = interval_floor(Interval("-1.7", "2.3")) # Rounds downward -> [-2, 2]
ceil_res  = interval_ceil(Interval("-1.7", "2.3"))  # Rounds upward -> [-1, 3]
```

---

## 11. Set Operations

`decoint` treats intervals geometrically as connected sets of real numbers. To resolve operations between multiple intervals, the engine exposes `intersection` and `hull` transformations. Unlike transcendental or power functions, these are structured as **instance methods** called directly on an initial interval object.

These methods accept another `Interval` or `DecoratedInterval` instance as their argument.

### Supported Set Methods
* **`intersection(other)`:** Returns the tightly bound segment where both intervals overlap. If no geometric overlap exists, it evaluates safely to an empty set representation (`EmptySet` / `NAI`).
* **`hull(other)`:** Returns the interval hull—the absolute smallest, continuous interval that entirely encloses both distinct sets, bridging any gaps between them.

```python
from decoint import Interval

i1 = Interval(1, 3)
i2 = Interval(2, 5)
i3 = Interval(6, 8)

# Intersection: Resolves the shared overlapping mathematical region
# Evaluates to [2, 3]
intersection_res = i1.intersection(i2)

# Hull: Spans the total domain from the lowest minimum to the highest maximum
# Evaluates to [1, 5]
hull_res = i1.hull(i2)

# Hull across disjoint sets: Safely bridges the gap between disconnected intervals
# Evaluates to [1, 8]
disjoint_hull = i1.hull(i3)
```

---

## 12. Unary Boolean Properties

`decoint` exposes a collection of state-interrogation tools as Python **properties**. These allow you to efficiently inspect the geometric and mathematical configuration of an interval without triggering execution overhead.

Because these components are implemented as properties rather than standard instance methods, **do not append trailing parentheses `()` when calling them.**

### Supported Boolean Properties
* **`is_empty`:** Returns `True` if the interval represents an empty set containing no real numbers.
* **`is_singleton`:** Returns `True` if the interval represents a singular exact value (a point interval where the lower bound equals the upper bound).
* **`is_bounded`:** Returns `True` if both the lower and upper bounds are finite real values (i.e., neither bound is infinity).
* **`is_entire`:** Returns `True` if the interval spans the entire mathematical real line from negative infinity to positive infinity.
* **`is_common`:** Returns `True` if the interval is both completely bounded and non-empty (representing a standard, standard-compliant bounded subset).

```python
from decoint import Interval

# Define various interval structures
i_standard  = Interval(1, 2)
i_point     = Interval("4.5")
i_inf       = Interval("-inf", "inf")

# Querying properties (Note the omission of parentheses)
print(i_standard.is_empty)     # Evaluates to False
print(i_standard.is_bounded)   # Evaluates to True
print(i_standard.is_common)    # Evaluates to True

# Geometrically isolated checks
print(i_point.is_singleton)    # Evaluates to True
print(i_inf.is_entire)         # Evaluates to True
```

---

## Numeric and Geometric Properties

In addition to boolean checks, `decoint` exposes regular unary properties that yield exact quantitative descriptions of an interval's topology and bounds. These are engineered as standard Python **properties** that return numeric values directly.

Like the boolean properties, these are zero-argument indicators. **Do not use parentheses `()` when querying them.**

### Supported Quantitative Properties

* **`inf` (Infimum):** Exposes the exact lower bound of the interval set.
* **`sup` (Supremum):** Exposes the exact upper bound of the interval set.
* **`width`:** The total distance spanned by the interval bounds (`sup - inf`). Returns infinity for unbounded sets.
* **`radius`:** Half of the interval's total width (`width / 2`).
* **`midpoint`:** The exact geographical center point of the interval set (`(inf + sup) / 2`).
* **`magnitude`:** The maximum absolute value mapped within the interval set. Mathematically defined as `max(|inf|, |sup|)`.
* **`mignitude`:** The minimum absolute value mapped within the interval set. Returns `0` if the interval encloses zero; otherwise, evaluates to `min(|inf|, |sup|)`.

### Code Example

```python
from decoint import Interval

# Instantiate a non-symmetric interval spanning across zero
i = Interval(-2, 4)

# Basic bound retrieval
print(i.inf)        # Evaluates to -2
print(i.sup)        # Evaluates to 4

# Geometric proportions
print(i.width)      # Evaluates to 6
print(i.radius)     # Evaluates to 3
print(i.midpoint)   # Evaluates to 1

# Absolute limits (Magnitude vs Mignitude)
print(i.magnitude)  # Evaluates to 4 (since |-2| is less than |4|)
print(i.mignitude)  # Evaluates to 0 (since the interval crosses zero)

# Mignitude on an interval strictly isolated from zero
i_positive = Interval(2, 5)
print(i_positive.mignitude)  # Evaluates to 2
```

---

## Lattice Operations

Intervals form a bounded lattice under the standard coordinate-wise product order. To compute the lattice infimum and supremum between two intervals, `decoint` exposes the `interval_min` and `interval_max` binary functions. 

These operations are structurally distinct from standard set operations (like intersection or hull) because they compute the minimum or maximum of the respective upper and lower bounds directly, rather than treating the intervals as point sets.

### Supported Lattice Functions

* **`interval_min(x, y)`:** Computes the lower bound as the minimum of the two lower bounds, and the upper bound as the minimum of the two upper bounds: `[min(x.inf, y.inf), min(x.sup, y.sup)]`.
* **`interval_max(x, y)`:** Computes the lower bound as the maximum of the two lower bounds, and the upper bound as the maximum of the two upper bounds: `[max(x.inf, y.inf), max(x.sup, y.sup)]`.

### Code Example

```python
from decoint import Interval, interval_min, interval_max

# Define two overlapping, staggered intervals
i1 = Interval(1, 5)
i2 = Interval(3, 4)

# Lattice Minimum (Infimum)
# Lower bound: min(1, 3) = 1
# Upper bound: min(5, 4) = 4
# Evaluates to [1, 4]
min_res = interval_min(i1, i2)

# Lattice Maximum (Supremum)
# Lower bound: max(1, 3) = 3
# Upper bound: max(5, 4) = 5
# Evaluates to [3, 5]
max_res = interval_max(i1, i2)
```

---

Markdown
## Set Relations and Comparisons

Intervals can be evaluated topologically and geometrically to determine how they nest, overlap, or position themselves relative to one another on the real number line. In `decoint`, these relations are exposed primarily as instance methods returning boolean values, with standard relational operators overloaded for intuitive comparison syntax.

### 1. Inclusion and Overlap Relations

These methods allow you to test for subset conditions, containment, and intersections between intervals or point values.

* **`subset(other)`**: Returns `True` if every element of the current interval is contained within the `other` interval.
* **`proper_subset(other)`**: Returns `True` if the current interval is a subset of `other`, but the two intervals are not identical.
* **`contains(x)`**: Unlike other relational methods, this checks element membership and accepts a **single numeric value** (integer, float, or `gmpy2` type) rather than an interval. It returns `True` if $x$ lies within the interval's bounds.
* **`interior(other)`**: Returns `True` if the current interval lies strictly inside the interior of `other` (meaning the bounds of the current interval do not touch the boundaries of `other`).
* **`overlaps(other)`**: Returns `True` if the two intervals share at least one common real number (a non-empty intersection).
* **`disjoint(other)`**: Returns `True` if there is absolutely no overlap between the two intervals (their intersection is completely empty).

### 2. Positional and Ordering Relations

These methods evaluate the strict directional ordering of two intervals across the real line.

* **`precedes(other)`**: Returns `True` if the current interval is completely to the left of `other`, or at most touches its lower bound.
* **`meets(other)`**: Returns `True` if the upper bound of the current interval exactly matches the lower bound of `other` without any overlapping interior.
* **`strictly_less_than(other)`**: Returns `True` if every element in the current interval is strictly less than every element in `other` (there is a visible gap between them).
* **`strictly_greater_than(other)`**: Returns `True` if every element in the current interval is strictly greater than every element in `other`.

### 3. Operator-Based Comparisons

For standard element-wise interval inequalities, `decoint` overloads Python's built-in comparison operators. These follow certain-order relational logic where the condition must hold true across all possible variations within the sets.

* **Less Than (`<`)**: Evaluates if the current interval is strictly to the left of another interval.
* **Greater Than (`>`)**: Evaluates if the current interval is strictly to the right of another interval.

### Code Example

```python
from decoint import Interval

# Define a baseline set of intervals for comparison
i1 = Interval(1, 3)
i2 = Interval(2, 5)
i3 = Interval(1, 3)
i4 = Interval(5, 7)

# 1. Inclusion and Overlap Tests
print(i1.subset(i2))           # Evaluates to False
print(Interval(2, 3).subset(i1)) # Evaluates to True
print(i1.proper_subset(i3))    # Evaluates to False (they are equal)
print(i1.overlaps(i2))         # Evaluates to True (overlap on [2, 3])
print(i1.disjoint(i4))         # Evaluates to True

# Element containment check (takes a scalar number)
print(i1.contains(2.5))        # Evaluates to True
print(i1.contains(4))          # Evaluates to False

# 2. Positional and Ordering Tests
print(i1.precedes(i4))         # Evaluates to True
print(i1.meets(i2))            # Evaluates to False
print(i1.meets(i4))            # Evaluates to False (gap between 3 and 5)
print(i1.strictly_less_than(i4)) # Evaluates to True

# 3. Operator-Based Inequalities
print(i1 < i4)                 # Evaluates to True
print(i4 > i2)                 # Evaluates to True
```
---






