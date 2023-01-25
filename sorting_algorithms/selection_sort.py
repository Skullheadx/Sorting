# Selection Sort (O(n^2))
from sorting_algorithms.utils import swap


def selection_sort(array):
    for index1 in range(len(array) - 1, 0, -1):  # loop through from end
        swap_index = 0  # largest element to swap with
        for index2 in range(index1 + 1):  # loop through the first index1 elements
            if array[index2] > array[swap_index]:  # find the max element to swap with
                swap_index = index2  # set the swap index
        swap(array, index1, swap_index)  # use swap the largest and the index1 (from end)
    return array  # return sorted array


def selection_sort_frames(array):
    frames = []
    for index1 in range(len(array) - 1, 0, -1):  # loop through from end
        swap_index = 0  # largest element to swap with
        for index2 in range(index1 + 1):  # loop through the first index1 elements
            if array[index2] > array[swap_index]:  # find the max element to swap with
                swap_index = index2  # set the swap index
        swap(array, index1, swap_index)  # use swap the largest and the index1 (from end)
        frames.append(array[:])
    return frames
