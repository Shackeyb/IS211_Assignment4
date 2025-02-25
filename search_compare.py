import time
import random


def get_me_random_list(n):
    """Generate list of n unique positive integers in random order"""
    a_list = list(range(1, n + 1))  # Positive integers only
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    """Performs Sequential Search and returns time taken"""
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found, time.time() - start_time


def ordered_sequential_search(a_list, item):
    """Performs Ordered Sequential Search and returns time taken"""
    start_time = time.time()
    a_list.sort()  # Sorting before searching
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos += 1

    return found, time.time() - start_time


def binary_search_iterative(a_list, item):
    """Performs Iterative Binary Search and returns time taken"""
    start_time = time.time()
    a_list.sort()  # Sorting before searching
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found, time.time() - start_time


def binary_search_recursive(a_list, item):
    """Performs Recursive Binary Search and returns time taken"""
    start_time = time.time()
    a_list.sort()  # Sorting before searching

    def helper(sub_list):
        if len(sub_list) == 0:
            return False
        midpoint = len(sub_list) // 2
        if sub_list[midpoint] == item:
            return True
        elif item < sub_list[midpoint]:
            return helper(sub_list[:midpoint])
        else:
            return helper(sub_list[midpoint + 1:])

    result = helper(a_list)
    return result, time.time() - start_time


def main():
    """Main function to benchmark search algorithms"""
    list_sizes = [500, 1000, 5000]
    num_trials = 100
    search_item = 99999999  # Item that does not exist

    for size in list_sizes:
        print(f"\nBenchmarking for list size {size}:")

        # Sequential Search
        total_time = sum(sequential_search(get_me_random_list(size), search_item)[1] for _ in range(num_trials))
        print(f"Sequential Search took {total_time / num_trials:10.7f} seconds on average.")

        # Ordered Sequential Search
        total_time = sum(ordered_sequential_search(get_me_random_list(size), search_item)[1] for _ in range(num_trials))
        print(f"Ordered Sequential Search took {total_time / num_trials:10.7f} seconds on average.")

        # Binary Search Iterative
        total_time = sum(binary_search_iterative(get_me_random_list(size), search_item)[1] for _ in range(num_trials))
        print(f"Binary Search Iterative took {total_time / num_trials:10.7f} seconds on average.")

        # Binary Search Recursive
        total_time = sum(binary_search_recursive(get_me_random_list(size), search_item)[1] for _ in range(num_trials))
        print(f"Binary Search Recursive took {total_time / num_trials:10.7f} seconds on average.")


if __name__ == "__main__":
    main()