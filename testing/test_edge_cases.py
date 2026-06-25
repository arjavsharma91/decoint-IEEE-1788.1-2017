from intervals.interval import Interval

EDGE_INTERVALS = [
    Interval.empty(),
    Interval.entire(),
    Interval(0, 0),
    Interval(-1, 1),
    Interval(1, 2),
    Interval(-5, -2),
    Interval(0, float('inf')),
    Interval(float('-inf'), 0)
]

def test_arithmetic_edge_matrix():
    """Runs an exhaustive combinatorial matrix check across edge configurations."""
    for x in EDGE_INTERVALS:
        for y in EDGE_INTERVALS:
            try:
                _ = x + y
                _ = x - y
                _ = x * y
                if not y.contains(0) and not y.is_empty:
                    _ = x / y
            except Exception as e:
                raise AssertionError(f"Crash detected during evaluation of {x} and {y}: {e}")
    print("✅ Edge case matrix completed safely.")
