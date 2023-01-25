# Insertion Sort (O(n^2))

def insertion_sort(array):
    for index1 in range(1, len(array)):  # look at second element
        for index2 in range(0, index1):  # loop through each of previous elements to find where to insert
            if array[index2] > array[index1]:  # find where in the sorted portion to put next element
                array.insert(index2, array[index1])  # insert smaller element into sorted portion
                del array[index1 + 1]  # +1 because inserted an element
                break  # already inserted element, move on to the next element
    return array  # return sorted array


def insertion_sort_frames(array):
    frames = []
    for index1 in range(1, len(array)):  # look at second element
        for index2 in range(0, index1):  # loop through each of previous elements to find where to insert
            if array[index2] > array[index1]:  # find where in the sorted portion to put next element
                array.insert(index2, array[index1])  # insert smaller element into sorted portion
                del array[index1 + 1]  # +1 because inserted an element
                frames.append(array[:])
                break  # already inserted element, move on to the next element

    return frames
