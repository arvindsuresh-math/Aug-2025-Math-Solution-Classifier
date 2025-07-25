def solve():
    """Index: 5734.
    Returns: the total number of times Darry has climbed a step today.
    """
    # L1
    full_ladder_steps = 11 # full ladder, which has 11 steps
    full_ladder_climbs = 10 # 10 times today
    full_ladder_total_steps = full_ladder_steps * full_ladder_climbs

    # L2
    smaller_ladder_steps = 6 # smaller ladder, which has 6 steps
    smaller_ladder_climbs = 7 # 7 times today
    smaller_ladder_total_steps = smaller_ladder_steps * smaller_ladder_climbs

    # L3
    total_steps_climbed = full_ladder_total_steps + smaller_ladder_total_steps

    # FA
    answer = total_steps_climbed
    return answer