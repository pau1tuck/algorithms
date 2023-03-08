# Time complexity: O(n^2)

import time
import os
import psutil

st = time.time()  # start time


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
    return my_list


def bubbleSort_optimized(my_list):
    n = len(my_list)
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):  # Traverse the array from 0 to n-i-1
            if my_list[j] > my_list[j + 1]:  # Swap if the element found is greater than the next element
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                swapped = True
        if not swapped:
            break


et = time.time()  # end time

elapsed_time = et - st


if __name__ == "__main__":
    # Test the algorithm
    array = [4, 2, 6, 5, 1, 3, 8, 7]

    print("Array length:", str(len(array)))
    print("CPU:", os.cpu_count(), "logical cores at", psutil.cpu_freq(), "GHz")
    print("Bubble sort:", bubble_sort(array))
    print("Execution time:", elapsed_time * 1000, "milliseconds")
