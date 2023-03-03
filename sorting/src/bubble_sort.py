# Time complexity: O(n^2)

import time
import os
import psutil

st = time.time()


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
    return my_list


et = time.time()

elapsed_time = et - st


if __name__ == "__main__":
    # Test the algorithm
    array = [4, 2, 6, 5, 1, 3, 8, 7]

    print("Array length:", str(len(array)))
    print("CPU:", os.cpu_count(), "logical cores at", psutil.cpu_freq(), "GHz")
    print("Bubble sort:", bubble_sort(array))
    print("Execution time:", elapsed_time * 1000, "milliseconds")
