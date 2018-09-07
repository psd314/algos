# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    length = len(weights)
    ratios = [ values[i]/weights[i] for i in range(len(weights)) ]
    
    j = 0
    while capacity > 0 and j < length:
        i = ratios.index(max(ratios))
        if weights[i] <= capacity:
            value += values[i]
            capacity -= weights[i]
            del weights[i]
            del values[i]
            del ratios[i]
        else:
            value += (capacity/weights[i]) * values[i]    
            capacity -= capacity/weights[i] * weights[i]       
        j += 1
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
