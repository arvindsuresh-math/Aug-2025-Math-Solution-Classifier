def solve():
    """Index: 4114.
    Returns: the number of laps Sarith ran around the children's football field.
    """
    # L1
    kristin_laps = 12 # Kristin runs 12 times around the adult football field
    speed_multiplier = 3 # Kristin can run three times faster than Sarith
    sarith_equivalent_laps_adult_field = kristin_laps / speed_multiplier

    # L2
    field_distance_ratio = 2 # children's football field that is half the distance as the other field
    sarith_laps_children_field = sarith_equivalent_laps_adult_field * field_distance_ratio

    # FA
    answer = sarith_laps_children_field
    return answer