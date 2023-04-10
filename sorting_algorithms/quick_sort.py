from sorting_algorithms.utils import swap, is_increasing
import random

def quick_sort_frames(array, start=0, end=None, frames=None):
    if frames is None:
        frames = []
        is_root = True
    else:
        is_root = False
    if end is None:
        end = len(array) - 1
    pivot = array[end]  # pivot is the last element
    i = start-1
    j = start
    while j < end:  # loop through each element
        if array[j] < pivot:  # if less than pivot, swap with i
            i += 1
            swap(array, i, j)
            frames.append(array[:])
        j += 1
    swap(array, i + 1, j)  # swap pivot with i + 1
    frames.append(array[:])
    pivot = i + 1  # set pivot to i + 1
    if start < pivot - 1:  # if there are elements to the left of pivot
        quick_sort_frames(array, start, pivot - 1, frames)  # sort the left side
    if pivot + 1 < end:  # if there are elements to the right of pivot
        quick_sort_frames(array, pivot + 1, end, frames)  # sort the right side
    if is_root:
        return frames
    else:
        return array  # return sorted array


# arr = [random.randint(0, 100) for _ in range(10)]
# print(arr)
# print(quick_sort(arr))
# print(is_increasing(arr))

# import random
#
# def partition(array, begin, end):
#     pivot_index = begin
#
#     for i in range(begin, end):
#         if array[i] < array[begin]:
#             pivot_index += 1
#             array[i], array[pivot_index] = array[pivot_index], array[i]
#
#     array[pivot_index], array[begin] = array[begin], array[pivot_index]
#
#     return pivot_index
#
# def quick_sort(array, begin, end):
#     if begin != end and begin + 1 != end:
#         pivot = partition(array, begin, end)
#
#         quick_sort(array, begin, pivot)
#
#         quick_sort(array, pivot + 1, end)
#
#
# array = [random.randint(0, 100) for _ in range(10)]
# print(array)
# quick_sort(array, 0, len(array))
# print(array)