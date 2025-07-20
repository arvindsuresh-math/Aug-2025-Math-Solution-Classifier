def solve():
    """Index: 5184.
    Returns: the amount of fabric Nguyen still needs in feet.
    """
    # L1
    fabric_per_pair = 8.5 # requires 8.5 feet of fabric
    num_pairs = 7 # needs to make 7 pairs of pants
    total_fabric_needed_feet = fabric_per_pair * num_pairs

    # L2
    fabric_has_yards = 3.5 # has 3.5 yards of fabric
    feet_per_yard = 3 # WK
    fabric_has_feet = fabric_has_yards * feet_per_yard

    # L3
    fabric_still_needed = total_fabric_needed_feet - fabric_has_feet

    # FA
    answer = fabric_still_needed
    return answer