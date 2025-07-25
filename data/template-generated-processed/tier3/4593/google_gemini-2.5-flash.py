def solve():
    """Index: 4593.
    Returns: the number of shampoo bottles Brittany needs.
    """
    # L1
    days_in_regular_year = 365 # WK
    days_shorter_leap_year = 1 # WK
    days_in_leap_year = days_in_regular_year - days_shorter_leap_year

    # L2
    wash_frequency_divisor = 2 # WK
    num_washes_leap_year = days_in_leap_year / wash_frequency_divisor

    # L3
    bottle_size_ounces = 14 # 14-ounce bottles
    shampoo_per_wash_numerator = 1 # 1/4 ounce of shampoo
    shampoo_per_wash_denominator = 4 # 1/4 ounce of shampoo
    washes_per_bottle = bottle_size_ounces / shampoo_per_wash_numerator / shampoo_per_wash_denominator

    # L4
    test_bottles_1 = 3 # WK
    washes_with_3_bottles = washes_per_bottle * test_bottles_1

    # L5
    test_bottles_2 = 4 # WK
    washes_with_4_bottles = washes_per_bottle * test_bottles_2

    # L6
    # FA
    answer = test_bottles_2
    return answer