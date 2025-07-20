def solve():
    """Index: 3202.
    Returns: how much less the new babysitter will cost.
    """
    # L1
    old_babysitter_rate = 16 # $16/hour
    hours_hired = 6 # hires the babysitter for 6 hours
    old_babysitter_cost = old_babysitter_rate * hours_hired

    # L2
    new_babysitter_rate = 12 # charges $12/hour
    new_babysitter_base_cost = new_babysitter_rate * hours_hired

    # L3
    num_screams = 2 # kids usually scream twice
    scream_charge_per_scream = 3 # extra $3 for each time the kids scream
    scream_cost = num_screams * scream_charge_per_scream

    # L4
    cost_difference = old_babysitter_cost - new_babysitter_base_cost - scream_cost

    # FA
    answer = cost_difference
    return answer