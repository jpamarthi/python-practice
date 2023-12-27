def find_sum_in_list(lst, s):
    flag = False
    # Step 1: Iterate each number in the outer loop
    for i in range(0, len(lst) - 1):
        # Step 2: Iterate through each number inner loop
        for j in range(i + 1, len(lst)):
            # Step 3: Add two numbers and see if we are getting to the sum
            if lst[i] + lst[j] == s:
                flag = True
                break
    # Step 4: Return True or False
    return flag
