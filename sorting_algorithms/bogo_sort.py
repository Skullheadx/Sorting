# Bogo Sort (O(n*n!))
from random import sample
from sorting_algorithms.utils import swap, is_increasing


def bogo_sort(array):
    while not is_increasing(array):  # repeat until completely sorted in ascending order
        a, b = sample(range(len(array)), 2)  # get two random indices
        swap(array, a, b)  # swap the two indices
    return array  # return the sorted array


def bogo_sort_frames(array):
    frames = []
    while not is_increasing(array):  # repeat until completely sorted in ascending order
        a, b = sample(range(len(array)), 2)  # get two random indices
        swap(array, a, b)  # swap the two indices
        frames.append(array[:])
    return frames
