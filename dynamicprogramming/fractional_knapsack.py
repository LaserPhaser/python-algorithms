def get_optimal_value(capacity, weights, values):
    value = 0.
    vperitem = [float(v) / float(w) for v,w in zip(values, weights)]
    weights = [x for (y,x) in reversed(sorted(zip(vperitem,weights)))]
    values = [x for (y,x) in reversed(sorted(zip(vperitem,values)))]
    for i in range(len(values)):
        if capacity == 0:
            return value
        willTake = min(capacity,weights[i])
        capacity  -= willTake
        value += (willTake) * (float(values[i])/(weights[i]))
    return value

