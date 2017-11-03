"""
Given weights and values of n items, we need put these items in a knapsack of capacity W to get
the maximum total value in the knapsack.
"""


def fractional_knapsack(capacity: int, items: [tuple]) -> float:
    """
    :param capacity: integer total capacity of backpack
    :param items: list of tuples [(value, weight),...]
    :return: float - maximum value that can be placed in backpack
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
