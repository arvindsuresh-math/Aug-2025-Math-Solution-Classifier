def solve():
    """Index: 366.
    Returns: the total length of ladders climbed by both workers in inches.
    """
    # L1
    keaton_ladder_length = 30 # 30 feet ladder
    keaton_climbs = 20 # climbed ... twenty times
    keaton_total_feet = keaton_ladder_length * keaton_climbs

    # L2
    reece_ladder_shorter_by = 4 # 4 feet shorter than Keaton's ladder
    reece_ladder_length = keaton_ladder_length - reece_ladder_shorter_by

    # L3
    reece_climbs = 15 # climbed ... 15 times
    reece_total_feet = reece_climbs * reece_ladder_length

    # L4
    total_feet = reece_total_feet + keaton_total_feet

    # L5
    inches_per_foot = 12 # WK
    total_inches = inches_per_foot * total_feet

    # FA
    answer = total_inches
    return answer