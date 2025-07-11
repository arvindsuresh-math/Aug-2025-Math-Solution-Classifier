def solve():
    """Index: 366.
    Returns: the total length climbed by both workers in inches.
    """
    # L1
    keaton_ladder_height = 30 # a 30 feet ladder
    keaton_climb_times = 20 # twenty times
    keaton_total_feet_climbed = keaton_ladder_height * keaton_climb_times

    # L2
    reece_ladder_shorter_by = 4 # 4 feet shorter than Keaton's ladder
    reece_ladder_height = keaton_ladder_height - reece_ladder_shorter_by

    # L3
    reece_climb_times = 15 # climbed a ladder 15 times
    reece_total_feet_climbed = reece_climb_times * reece_ladder_height

    # L4
    total_feet_climbed = reece_total_feet_climbed + keaton_total_feet_climbed

    # L5
    inches_per_foot = 12 # WK
    total_inches_climbed = inches_per_foot * total_feet_climbed

    # FA
    answer = total_inches_climbed
    return answer