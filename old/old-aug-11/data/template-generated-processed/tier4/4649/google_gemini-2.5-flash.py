def solve():
    """Index: 4649.
    Returns: the total number of minutes to fill the cans.
    """
    # L1
    total_cans_to_fill = 675 # 675 cans
    cans_per_group = 150 # 150 cans of paint every 8 minutes
    num_groups = total_cans_to_fill / cans_per_group

    # L2
    minutes_per_group = 8 # 8 minutes
    total_minutes = minutes_per_group * num_groups

    # FA
    answer = total_minutes
    return answer