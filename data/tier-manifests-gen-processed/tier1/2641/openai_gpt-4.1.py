def solve():
    """Index: 2641.
    Returns: the number of campers there were last week.
    """
    # L1
    campers_two_weeks_ago = 40 # there were 40 campers two weeks ago
    more_than_three_weeks_ago = 10 # which was 10 more than the number of campers three weeks ago
    campers_three_weeks_ago = campers_two_weeks_ago - more_than_three_weeks_ago

    # L2
    campers_first_two_weeks = campers_three_weeks_ago + campers_two_weeks_ago

    # L3
    total_campers = 150 # recorded a total of 150 campers for the past three weeks
    campers_last_week = total_campers - campers_first_two_weeks

    # FA
    answer = campers_last_week
    return answer