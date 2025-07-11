def solve():
    """Index: 2419.
    Returns: the number of rabbits the bear needs to catch each day.
    """
    # L1
    num_cubs = 4 # she has 4 cubs
    cub_meat_per_week = 35 # Each cub needs 35 pounds a week
    total_cub_meat_needed_per_week = num_cubs * cub_meat_per_week

    # L2
    bear_meat_per_week = 210 # She needs 210 pounds of meat in a week
    total_family_meat_needed_per_week = bear_meat_per_week + total_cub_meat_needed_per_week

    # L3
    days_per_week = 7 # WK
    meat_needed_per_day = total_family_meat_needed_per_week / days_per_week

    # L4
    rabbit_weight = 5 # rabbits, which are five pounds each
    rabbits_per_day = meat_needed_per_day / rabbit_weight

    # FA
    answer = rabbits_per_day
    return answer