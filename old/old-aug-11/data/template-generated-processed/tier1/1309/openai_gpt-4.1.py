def solve():
    """Index: 1309.
    Returns: the number of goldfish Martin will have in 7 weeks.
    """
    # L1
    goldfish_die_per_week = 5 # 5 goldfish die
    num_weeks = 7 # in 7 weeks
    total_goldfish_die = goldfish_die_per_week * num_weeks

    # L2
    goldfish_purchased_per_week = 3 # purchases 3 new goldfish every week
    total_goldfish_purchased = goldfish_purchased_per_week * num_weeks

    # L3
    initial_goldfish = 18 # Martin has 18 goldfish
    goldfish_after_7_weeks = initial_goldfish - total_goldfish_die + total_goldfish_purchased

    # FA
    answer = goldfish_after_7_weeks
    return answer