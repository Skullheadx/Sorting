# Bogo Sort (O(n*n!))
from random import sample
from utils import swap, is_increasing


def bogo_sort(array):
    while not is_increasing(array):
        a, b = sample(range(len(array)), 2)
        swap(array, a, b)
    return array
