def solve():
    """Index: 98.
    Returns: the total number of gumballs that Hector purchased.
    """
    # L1
    gumballs_to_todd = 4 # gave 4 to Todd
    multiplier_twice = 2 # twice as many as he had given Todd
    gumballs_to_alisha = gumballs_to_todd * multiplier_twice

    # L2
    less_than_four_times = 5 # 5 less than four times as many
    multiplier_four_times = 4 # four times as many
    gumballs_to_bobby = (gumballs_to_alisha * multiplier_four_times) - less_than_four_times

    # L3
    gumballs_remaining = 6 # 6 gumballs remaining
    total_gumballs_purchased = gumballs_to_todd + gumballs_to_alisha + gumballs_to_bobby + gumballs_remaining

    # FA
    answer = total_gumballs_purchased
    return answer