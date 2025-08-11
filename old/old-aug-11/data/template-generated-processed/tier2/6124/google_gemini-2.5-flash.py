def solve():
    """Index: 6124.
    Returns: the amount of fabric Amare still needs in feet.
    """
    # L1
    fabric_per_dress_yards = 5.5 # 5.5 yards of fabric
    num_dresses = 4 # make 4 dresses
    total_fabric_needed_yards = fabric_per_dress_yards * num_dresses

    # L2
    feet_per_yard = 3 # WK
    total_fabric_needed_feet = total_fabric_needed_yards * feet_per_yard

    # L3
    fabric_on_hand_feet = 7 # has 7 feet of fabric
    fabric_still_needed_feet = total_fabric_needed_feet - fabric_on_hand_feet

    # FA
    answer = fabric_still_needed_feet
    return answer