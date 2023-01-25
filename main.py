import random
from display import Display
from sorting_algorithms.bubble_sort import bubble_sort, bubble_sort_frames

def main():
    array = [random.randint(10, 50) for _ in range(75)]
    frames = bubble_sort_frames(array)
    window = Display(frames)
    window.show()


if __name__ == "__main__":
    main()
