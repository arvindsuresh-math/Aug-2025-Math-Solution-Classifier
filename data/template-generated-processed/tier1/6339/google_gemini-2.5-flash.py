def solve():
    """Index: 6339.
    Returns: the total quantity of oranges bought after three weeks.
    """
    # L1
    initial_oranges = 10 # buys 10kgs of oranges
    added_oranges = 5 # add 5 more kgs
    first_week_total = initial_oranges + added_oranges

    # L2
    multiplier_twice = 2 # twice as many oranges
    next_week_quantity = multiplier_twice * first_week_total

    # L3
    num_weeks_for_total = 2 # next coming two weeks
    total_next_two_weeks = next_week_quantity * num_weeks_for_total

    # L4
    total_three_weeks = total_next_two_weeks + first_week_total

    # FA
    answer = total_three_weeks
    return answer