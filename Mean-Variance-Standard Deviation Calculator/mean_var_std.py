import numpy as np


def calculate(list):
    if 9 > len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    flattened_mean = np.mean(list)
    flattened_var = np.var(list)
    flattened_std = np.std(list)
    flattened_max = np.max(list)
    flattened_min = np.min(list)
    flattened_sum = np.sum(list)

    arr = np.array(list)  # change to numpy array
    arr3x3 = arr.reshape(3, 3)  # reshape to 3x3

    # mean
    arr_mean_ax0 = np.mean(arr3x3, axis=0)
    arr_mean_ax1 = np.mean(arr3x3, axis=1)

    # variance
    arr_var_ax0 = np.var(arr3x3, axis=0)
    arr_var_ax1 = np.var(arr3x3, axis=1)

    # standard deviation
    arr_std_ax0 = np.std(arr3x3, axis=0)
    arr_std_ax1 = np.std(arr3x3, axis=1)

    # max
    arr_max_ax0 = np.max(arr3x3, axis=0)
    arr_max_ax1 = np.max(arr3x3, axis=1)

    # min
    arr_min_ax0 = np.min(arr3x3, axis=0)
    arr_min_ax1 = np.min(arr3x3, axis=1)

    # sum
    arr_sum_ax0 = np.sum(arr3x3, axis=0)
    arr_sum_ax1 = np.sum(arr3x3, axis=1)

    calculations = {'mean': [arr_mean_ax0.tolist(), arr_mean_ax1.tolist(), flattened_mean],
                    'variance': [arr_var_ax0.tolist(), arr_var_ax1.tolist(), flattened_var],
                    'standard deviation': [arr_std_ax0.tolist(), arr_std_ax1.tolist(), flattened_std],
                    'max': [arr_max_ax0.tolist(), arr_max_ax1.tolist(), flattened_max],
                    'min': [arr_min_ax0.tolist(), arr_min_ax1.tolist(), flattened_min],
                    'sum': [arr_sum_ax0.tolist(), arr_sum_ax1.tolist(), flattened_sum]}

    return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
