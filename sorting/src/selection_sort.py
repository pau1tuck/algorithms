def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1), len(my_list):
            if my_list[j] < min_index:
                min_index = j
        if i != min_index:  # if i and j are equal there is no need to swap them
            # swap i and min_index
            tmp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = tmp
