def solve():
    """Index: 1959.
    Returns: the amount of money Abigail has lost.
    """
    # L1
    initial_money = 11 # $11 in her purse at the start of the day
    spent = 2 # she spent $2 in a store
    expected_left = initial_money - spent

    # L2
    actual_left = 3 # she now has $3 left
    money_lost = expected_left - actual_left

    # FA
    answer = money_lost
    return answer