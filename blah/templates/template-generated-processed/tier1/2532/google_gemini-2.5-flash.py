def solve():
    """Index: 2532.
    Returns: the number of additional cans Kaiden needs to collect.
    """
    # L1
    cans_first_week = 158 # 158 cans during his first week
    cans_second_week = 259 # 259 during the second week
    total_collected_cans = cans_first_week + cans_second_week

    # L2
    goal_cans = 500 # goal is to collect 500 cans
    cans_needed = goal_cans - total_collected_cans

    # FA
    answer = cans_needed
    return answer