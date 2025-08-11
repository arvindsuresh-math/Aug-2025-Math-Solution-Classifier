def solve():
    """Index: 7409.
    Returns: the number of days Bill's toilet paper supply will last.
    """
    # L1
    num_rolls = 1000 # 1000 rolls of toilet paper
    squares_per_roll = 300 # each roll has 300 squares of toilet paper
    total_squares = num_rolls * squares_per_roll

    # L2
    squares_per_use = 5 # uses 5 squares of toilet paper each time
    uses_per_day = 3 # goes to the bathroom three times a day
    squares_per_day = squares_per_use * uses_per_day

    # L3
    days_supply_lasts = total_squares / squares_per_day

    # FA
    answer = days_supply_lasts
    return answer