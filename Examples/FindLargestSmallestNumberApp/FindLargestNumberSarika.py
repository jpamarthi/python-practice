def find_largest_two_numbers(number1, number2):
    # Choose the larger number
    if number1 > number2:
        larger_number = number1
    else:
        larger_number = number2
    return larger_number


def find_largest_three_numbers(number1, number2, number3):
    # We temporarily assume that the first number
    # is the largest one.
    # We will verify this soon.
    largest_number = number1

    # We check if the second number is larger than current largest_number
    # and update largest_number if needed.
    if number2 > largest_number:
        largest_number = number2

    # We check if the third number is larger than current largest_number
    # and update largest_number if needed.
    if number3 > largest_number:
        largest_number = number3

    return largest_number


def find_smallest_two_numbers(number1, number2):
    # Choose the smaller number
    if number1 < number2:
        smaller_number = number1
    else:
        smaller_number = number2
    return smaller_number
