def sorting_list_bubble_sort(my_list):
    swapped = True  # It's a little fake, we need it to enter the while loop.

    while swapped:
        swapped = False  # no swaps so far
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True  # a swap occurred!
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return my_list
