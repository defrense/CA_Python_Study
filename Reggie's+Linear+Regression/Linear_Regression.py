"""
This is a practice projects on list/loop concepts from CodeAcademy
codes use trial and error approach to find the best linear parameter of
a given data sets
"""

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
possible_ms = [ms * 0.1 for ms in range (-100, 100)]
possible_bs = [ms * 0.1 for ms in range (-200, 200)]
smallest_error = float('inf')
best_m = 0
best_b = 0

def get_y(m, b, x):
    y = m * x + b
    return y

def calculate_error(m, b, point):
    x_value, y_value = point
    y_point = get_y(m, b, x_value)
    distance = abs(y_point - y_value)
    return distance

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        total_error += calculate_error(m, b, point)
    return total_error


def calculate_best_mb(possible_ms, possible_bs, datapoints):
    smallest_error = float('inf')
    for ms in possible_ms:
        for bs in possible_bs:
            calculate_all_error_result = calculate_all_error(ms, bs, datapoints)
            if calculate_all_error_result < smallest_error :
                smallest_error = calculate_all_error_result
                best_m = ms
                best_b = bs
    return best_m, best_b


result = calculate_best_mb(possible_ms, possible_bs, datapoints)

print (result)

m, b = result

print (get_y(0.3, 1.7, 6))
