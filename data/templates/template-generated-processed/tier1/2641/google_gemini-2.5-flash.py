def solve():
    """Index: 2641.
    Returns: the number of campers last week.
    """
    # L1
    campers_two_weeks_ago = 40 # 40 campers
    more_than_three_weeks_ago = 10 # 10 more than the number of campers three weeks ago
    campers_three_weeks_ago = campers_two_weeks_ago - more_than_three_weeks_ago

    # L2
    total_three_and_two_weeks_ago = campers_three_weeks_ago + campers_two_weeks_ago

    # L3
    total_campers_three_weeks = 150 # a total of 150 campers for the past three weeks
    campers_last_week = total_campers_three_weeks - total_three_and_two_weeks_ago

    # FA
    answer = campers_last_week
    return answer