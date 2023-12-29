def find_sum_in_list(lst, s):
    # Step 1: Iterate each number in the outer loop
    for i in range(0, len(lst) - 1):
        # Step 2: Iterate through each number inner loop
        for j in range(i + 1, len(lst)):
            # Step 3: Add two numbers and see if we are getting to the sum
            if lst[i] + lst[j] == s:
                return True
    # Step 4: Return True or False
    return False


def find_sum_in_list_3(lst, s):
    i = 0
    j = -1
    # Step 1: Iterate through the list from both directions
    while True:
        # Step 2: Add the first and last elements
        result_sum = lst[i] + lst[j]
        # Step 3: Check if the result is greater or lesser or equal
        # Step 4: If it is equal return True
        if result_sum == s:
            return True
        # Step 5: If the sum is greater, then move the ending pointer backwards
        elif result_sum > s:
            j -= 1
        # Step 6: If the sum is less, then move the starting pointer forward
        else:
            i += 1

    # Step 7: Return False since there are no matches
    return False
