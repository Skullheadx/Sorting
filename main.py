import random
from display import Display
from sorting_algorithms.insertion_sort import insertion_sort_frames
from sorting_algorithms.selection_sort import selection_sort_frames
from sorting_algorithms.bogo_sort import bogo_sort_frames
from sorting_algorithms.bubble_sort import bubble_sort_frames
from sorting_algorithms.quick_sort import quick_sort


def main():
    array = [random.random() for _ in range(500)]
    frames = quick_sort(array)
    window = Display(frames)
    window.show()


if __name__ == "__main__":
    main()
