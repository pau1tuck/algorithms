# Time complexity: O(n^2)


def selection_sort(my_list):
    for i in range(len(my_list) - 1):  # 1 --> 8
        min_index = i  # i = 1
        for j in range(i + 1), len(my_list):  # 2 --> 8
            if my_list[j] < min_index:  # if 6 < 1
                min_index = j
        if i != min_index:  # if i and j are equal there is no need to swap them
            # swap i and min_index
            tmp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = tmp
    return my_list


array = [4, 2, 6, 5, 1, 3, 8, 7]

print(selection_sort(array))
