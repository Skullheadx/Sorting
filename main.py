import random
from display import Display
from sorting_algorithms.insertion_sort import insertion_sort_frames
from sorting_algorithms.selection_sort import selection_sort_frames
from sorting_algorithms.bogo_sort import bogo_sort_frames
from sorting_algorithms.bubble_sort import bubble_sort_frames


def main():
    array = [random.random() for _ in range(50)]
    frames = bubble_sort_frames(array)
    window = Display(frames)
    window.show()


if __name__ == "__main__":
    main()
