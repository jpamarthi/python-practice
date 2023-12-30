def find_sum_in_list_approach1(lst, s):
    # Step 1: Iterate each number in the outer loop
    for i in range(0, len(lst) - 1):
        # Step 2: Iterate through each number inner loop
        for j in range(i + 1, len(lst)):
            # Step 3: Add two numbers and see if we are getting to the sum
            if lst[i] + lst[j] == s:
                return True
    # Step 4: Return True or False
    return False


def find_sum_in_lst_approach2(lst, s):
    # Step 1: Iterate each number in the list
    for i in range(0, len(lst)-1):
        # Step 2: Subtract each number from Sum and use the result to search
        find = s - lst[i]
        # Step 3: Find sum in the sublist
        if find in lst[i+1:]:
            return True
    # Step 4: Return the result
    return False
