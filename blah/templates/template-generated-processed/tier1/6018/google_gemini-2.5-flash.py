def solve():
    """Index: 6018.
    Returns: the total number of brownies Katy made.
    """
    # L1
    brownies_monday = 5 # eats 5 on Monday
    multiplier_tuesday = 2 # twice as many on Tuesday
    brownies_tuesday = brownies_monday * multiplier_tuesday

    # L2
    total_brownies_made = brownies_monday + brownies_tuesday

    # FA
    answer = total_brownies_made
    return answer