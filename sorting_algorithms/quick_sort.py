import random


def partition(array, begin, end, frames):
    pivot_index = begin

    for i in range(begin, end):
        if array[i] < array[begin]:
            pivot_index += 1
            array[i], array[pivot_index] = array[pivot_index], array[i]
            frames.append(array[:])

    array[pivot_index], array[begin] = array[begin], array[pivot_index]
    frames.append(array[:])

    return pivot_index


def quick_sort(array, begin=0, end=None, frames=None):
    if frames is None:
        frames = []

    if end is None:
        end = len(array)

    if begin != end and begin + 1 != end:
        pivot = partition(array, begin, end, frames)

        quick_sort(array, begin, pivot, frames)

        quick_sort(array, pivot + 1, end, frames)

    return frames


array = [random.randint(0, 100) for _ in range(10)]
print(array)
quick_sort(array, 0, len(array), [])
print(array)