def solve():
    """Index: 5087.
    Returns: how much more cakes Carter was able to bake for this week.
    """
    # L1
    cheesecakes_regular = 6 # bakes 6 cheesecakes
    muffins_regular = 5 # 5 muffins
    red_velvet_cakes_regular = 8 # 8 red velvet cakes regularly
    regular_cakes_total = cheesecakes_regular + muffins_regular + red_velvet_cakes_regular

    # L2
    triple_multiplier = 3 # triple the number
    cheesecakes_this_week = cheesecakes_regular * triple_multiplier

    # L3
    muffins_this_week = muffins_regular * triple_multiplier

    # L4
    red_velvet_cakes_this_week = red_velvet_cakes_regular * triple_multiplier

    # L5
    total_cakes_this_week = cheesecakes_this_week + muffins_this_week + red_velvet_cakes_this_week

    # L6
    more_cakes_this_week = total_cakes_this_week - regular_cakes_total

    # FA
    answer = more_cakes_this_week
    return answer