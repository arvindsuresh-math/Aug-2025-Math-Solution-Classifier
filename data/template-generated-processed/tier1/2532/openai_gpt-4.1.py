def solve():
    """Index: 2532.
    Returns: the number of cans Kaiden still needs to collect to reach his goal.
    """
    # L1
    first_week = 158 # collects 158 cans during his first week
    second_week = 259 # 259 during the second week
    total_collected = first_week + second_week

    # L2
    goal = 500 # his goal is to collect 500 cans
    cans_needed = goal - total_collected

    # FA
    answer = cans_needed
    return answer