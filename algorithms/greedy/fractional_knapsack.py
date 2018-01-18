"""
Given weights and values of n items, we need put these items in a knapsack of capacity W to get
the maximum total value in the knapsack.

Complexity: O(n log n)
"""


def fractional_knapsack(capacity: int, items: [tuple]) -> float:
    """
    Function solves fractional knapsack problem

    Args:
        capacity: total capacity of backpack
        items: list of tuples [(value, weight),...]

    Returns:
        float - maximum value that can be placed in backpack

    Examples:
        >>> fractional_knapsack(50, [(60, 10), (100, 20), (120, 30)])
        240.0
    """

    value = 0.
    v_per_item = [float(v) / float(w) for v, w in items]
    weights = [x[1] for (y, x) in reversed(sorted(zip(v_per_item, items)))]
    values = [x[0] for (y, x) in reversed(sorted(zip(v_per_item, items)))]
    for i in range(len(values)):
        if capacity == 0:
            return value
        will_take = min(capacity, weights[i])
        capacity -= will_take
        value += will_take * (float(values[i]) / (weights[i]))
    return value
