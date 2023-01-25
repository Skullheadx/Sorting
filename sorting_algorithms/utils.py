def swap(array, index1, index2):
    get = array[index1], array[index2]
    array[index2], array[index1] = get
    return array


def is_increasing(array):
    for index in range(len(array)-1):
        if array[index] > array[index + 1]:
            return False
    return True
