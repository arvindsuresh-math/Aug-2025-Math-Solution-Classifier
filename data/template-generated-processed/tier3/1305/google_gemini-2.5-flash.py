def solve():
    """Index: 1305.
    Returns: the number of bats Randy has.
    """
    # L1
    total_gloves = 29 # If he has 29 baseball gloves
    more_than = 1 # 1 more baseball glove
    seven_times_bats = total_gloves - more_than

    # L2
    multiplier = 7 # 7 times the number of bats
    number_of_bats = seven_times_bats / multiplier

    # FA
    answer = number_of_bats
    return answer