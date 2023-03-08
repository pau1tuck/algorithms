# Insertion Sort (O=n^2)


def insertion_sort(my_list):
    for i in range(1, len(my_list)):  # start at my_list[1]
        tmp = my_list[i]  # e.g. tmp = my_list[4]
        j = i - 1  # 3
        while tmp < my_list[j] and j > -1:  # my_list[4] < my_list[3], # edge case: j cannot be -1
            my_list[j + 1] = my_list[j]  # my_list[4] becomes my_list[3]
            my_list[j] = tmp  # my_list[3] becomes my_list[4] (tmp)
            j -= 1  # slide my_list[3] to my_list[2] and run the loop again
    return my_list


print("[4, 2, 6, 5, 1, 3, 8, 7]")
print(insertion_sort([4, 2, 6, 5, 1, 3, 8, 7]))
