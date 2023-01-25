# Bubble Sort (O(n^2))
from sorting_algorithms.utils import swap


def bubble_sort(array):
    for top in range(len(array) - 1, 0, -1):  # loop through each element from end
        is_sorted = True  # to end early if already sorted
        for index in range(top):  # loop through each of elements until reach top
            if array[index] > array[index + 1]:  # if greater, swap
                swap(array, index, index + 1)  # swap with next
                is_sorted = False  # reset to not sorted
        if is_sorted:  # break out if already sorted
            break
    return array  # return sorted array


def bubble_sort_frames(array):
    frames = []
    for top in range(len(array) - 1, 0, -1):  # loop through each element from end
        is_sorted = True  # to end early if already sorted
        for index in range(top):  # loop through each of elements until reach top
            if array[index] > array[index + 1]:  # if greater, swap
                swap(array, index, index + 1)  # swap with next
                is_sorted = False  # reset to not sorted
                frames.append(array[:])
        if is_sorted:  # break out if already sorted
            break
    return frames
