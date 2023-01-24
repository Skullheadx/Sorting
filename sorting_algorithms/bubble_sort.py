# Bubble Sort (O(n^2))
from utils import swap


def bubble_sort(array):
    for index1 in range(len(array)):  # loop through each element
        for index2 in range(index1, len(array)):  # loop through each of the next elements
            if array[index2] < array[index1]:  # if lesser, then swap
                swap(array, index1, index2)
    return array  # return sorted array

