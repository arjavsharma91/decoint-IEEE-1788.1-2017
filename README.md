[![CI Tests](https://github.com/arjavsharma91/decoint-IEEE-1788.1-2017/actions/workflows/tests.yml/badge.svg)](https://github.com/arjavsharma91/decoint-IEEE-1788.1-2017/actions/workflows/tests.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![IEEE Standard](https://img.shields.io/badge/IEEE-1788.1--2017%20Compliant-green)](https://standards.ieee.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**decoint** is a fully compliant Python implementation of the **IEEE 1788.1-2017 Standard for Interval Arithmetic**. 

Designed for verified numerical computing, validated global optimization, and reliable scientific calculations, `decoint` achieves **100% completion across ~5,000 test cases** pulled directly from the official **ITF1788** compliance test suite repository.

---

## Key Features

* **Full IEEE 1788.1-2017 Conformance:** Implements exact standard requirements for interval arithmetic, elementary functions, decorations, classtypes, and set relations.
* **String Parsing & Text Conversion:** Accurate text-to-interval parsing and string formatting adhering strictly to standard directed rounding rules.
* **Extensive Test Coverage:** Battle-tested against ~5,000 test cases from ITF1788 covering arithmetic, set operations, mathematical functions, and edge cases.
* **Pure Python Portability:** Lightweight setup with no heavy external dependencies, installing seamlessly via `pip`.

---

## Installation

### Standard Install
Clone the repository and install `decoint` locally:

```bash
git clone [https://github.com/arjavsharma91/decoint-IEEE-1788.1-2017.git](https://github.com/arjavsharma91/decoint-IEEE-1788.1-2017.git)
cd decoint-IEEE-1788.1-2017
pip install .
```

### Development Mode
For local development and running the test suite:

```bash
pip install -e .
pip install pytest
```

---

## Quickstart

```python
from decoint import Interval

# Create intervals from floating-point values or text representations
a = Interval(1.0, 2.0)
b = Interval("[3.0, 4.0]")

# Standard Interval Arithmetic
c = a + b
print(c)  # [4.0, 6.0]

# Interval Functions & Set Relations
d = sin(a)
print(a.subset(c))  # False

# Bounds & Properties Access
print(f"Lower bound: {a.lo}, Upper bound: {a.hi}")
```

For detailed API guides, tutorials, and advanced examples, check [`documentation/usage.md`](usage.md).

---

## Testing & Conformance

We use `pytest` to run our test suite, which includes tests derived from the ITF1788 repository.

To run the full test suite locally:

```bash
python -m pytest
```

Refer to [`documentation/CONFORMANCE.md`](Conformance.md) for a complete breakdown of IEEE 1788.1-2017 clause coverage and verification results.

---

## Contributing

Contributions, bug reports, and improvements are welcome! Please review [`documentation/contributing.md`](CONTRIBUTING.md) before submitting pull requests or opening issues.

---
## License

Distributed under the [MIT License](LICENSE).
