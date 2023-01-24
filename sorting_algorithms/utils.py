def swap(array, index1, index2):
    get = array[index1], array[index2]
    array[index2], array[index1] = get
    return array
