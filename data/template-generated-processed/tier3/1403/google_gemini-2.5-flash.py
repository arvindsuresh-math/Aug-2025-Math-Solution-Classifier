def solve():
    """Index: 1403.
    Returns: Brad's zip code.
    """
    # L1
    total_sum_of_five_numbers = 10 # five numbers that add up to 10
    sum_of_fourth_and_fifth = 8 # The fourth and fifth numbers add up to 8
    sum_of_first_three_numbers = total_sum_of_five_numbers - sum_of_fourth_and_fifth

    # L2
    third_number = 0 # The third number is zero
    sum_of_first_two_numbers = sum_of_first_three_numbers - third_number

    # L3
    divisor_for_equal_numbers = 2 # The first and second numbers are the same
    first_second_number = sum_of_first_two_numbers / divisor_for_equal_numbers

    # L4
    double_factor = 2 # double the first number
    fourth_number = double_factor * first_second_number

    # L5
    fifth_number = sum_of_fourth_and_fifth - fourth_number

    # L6
    # FA
    answer = f"{int(first_second_number)}{int(first_second_number)}{int(third_number)}{int(fourth_number)}{int(fifth_number)}"
    return answer