"""
The knapsack problem or rucksack problem is a problem in combinatorial optimization:
Given a set of items, each with a weight, determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit.
"""


def optimal_weight(capacity, weights):
    """
    Function calculate optimal_weight for rucksack from given list of weights
    :param capacity: max capacity of rucksack
    :param weights: list of weights
    :return: max possible weight that meet <= max capacity
    """
    weight_idx = 0
    possible_capacity = 0
    combinations = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    for weight_idx in range(1, len(weights) + 1):
        for possible_capacity in range(1, capacity + 1):
            combinations[weight_idx][possible_capacity] = combinations[weight_idx - 1][possible_capacity]
            if weights[weight_idx - 1] <= possible_capacity:
                val = weights[weight_idx - 1] \
                      + combinations[weight_idx - 1][possible_capacity - weights[weight_idx - 1]]
                if combinations[weight_idx][possible_capacity] < val:
                    combinations[weight_idx][possible_capacity] = val
    return combinations[weight_idx][possible_capacity]
