# Uses python3
import sys
import math
import random


def naive_minimum_distance(x, y):
    # write your code here
    if len(x) == 1:
        return 0
    min_d = math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
    for x1 in range(len(x)):
        for x2 in range(len(x)):
            if (x1 != x2) and math.sqrt((x[x1] - x[x2]) ** 2 + (y[x1] - y[x2]) ** 2) < min_d:
                min_d = math.sqrt((x[x1] - x[x2]) ** 2 + (y[x1] - y[x2]) ** 2)
    return min_d


def minimum_distance(x, y):
    if len(x) == 1:
        return 0
    if len(x) >= 4:
        ave = len(x) // 2
        '''
        print ("groups:")
        prinx   t (x[:ave], y[:ave])
        print (x[ave:], y[ave:])
        '''
        min_d1 = minimum_distance(x[:ave], y[:ave])
        min_d2 = minimum_distance(x[ave:], y[ave:])
        min_d = min(min_d1, min_d2)
        # print("min_d", min_d)
    else:
        min_d = math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
        for x1 in range(len(x)):
            for x2 in range(len(x)):
                if (x1 != x2) and math.sqrt((x[x1] - x[x2]) ** 2 + (y[x1] - y[x2]) ** 2) < min_d:
                    min_d = math.sqrt((x[x1] - x[x2]) ** 2 + (y[x1] - y[x2]) ** 2)
    return min_d

