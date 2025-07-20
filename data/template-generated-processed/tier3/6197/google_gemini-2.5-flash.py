def solve():
    """Index: 6197.
    Returns: the value of the third number.
    """
    # L2
    total_sum = 500 # The sum of the three numbers is 500
    first_number = 200 # the first number is 200
    sum_second_third = total_sum - first_number

    # L5
    # The coefficient_of_x is derived from the problem statement: if the third number is x, and the second number is twice the third (2x), then their sum is x + 2x = 3x.
    coefficient_of_x = 3 # derived from problem structure
    third_number_value = sum_second_third / coefficient_of_x

    # L6
    # FA
    answer = third_number_value
    return answer