def solve():
    """Index: 5996.
    Returns: the total number of apples produced by the tree in the first three years.
    """
    # L1
    first_year_apples = 40 # produces 40 apples in its first year

    # L2
    more_than_double = 8 # 8 more than double the amount
    double_factor = 2 # double the amount
    second_year_apples = more_than_double + double_factor * first_year_apples

    # L3
    reduction_divisor = 4 # production went down by a fourth
    third_year_apples = second_year_apples - second_year_apples / reduction_divisor

    # L4
    total_apples = first_year_apples + second_year_apples + third_year_apples

    # FA
    answer = total_apples
    return answer