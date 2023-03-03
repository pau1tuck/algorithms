import time

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

print(bubble_sort([4, 2, 6, 5, 1, 3, 8, 7]))
print("Execution time:", elapsed_time, "seconds")
