import time
import random


def get_me_random_list(n):
    """Generate list of n unique random positive integers"""
    a_list = list(range(1, n + 1))  # Positive integers only
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    """Performs Insertion Sort and returns time taken"""
    start_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

    return time.time() - start_time


def shell_sort(a_list):
    """Performs Shell Sort and returns time taken"""
    start_time = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2  # Reduce gap size

    return time.time() - start_time


def gap_insertion_sort(a_list, start, gap):
    """Helper function for Shell Sort"""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap

        a_list[position] = current_value


def python_sort(a_list):
    """Performs Python's built-in sort and returns time taken"""
    start_time = time.time()
    a_list.sort()
    return time.time() - start_time


def main():
    """Main function to benchmark sorting algorithms"""
    list_sizes = [500, 1000, 5000]
    num_trials = 100

    for size in list_sizes:
        print(f"\nBenchmarking for list size {size}:")

        # Python Sort
        total_time = sum(python_sort(get_me_random_list(size)) for _ in range(num_trials))
        print(f"Python Sort took {total_time / num_trials:10.7f} seconds on average.")

        # Insertion Sort
        total_time = sum(insertion_sort(get_me_random_list(size)) for _ in range(num_trials))
        print(f"Insertion Sort took {total_time / num_trials:10.7f} seconds on average.")

        # Shell Sort
        total_time = sum(shell_sort(get_me_random_list(size)) for _ in range(num_trials))
        print(f"Shell Sort took {total_time / num_trials:10.7f} seconds on average.")


if __name__ == "__main__":
    main()