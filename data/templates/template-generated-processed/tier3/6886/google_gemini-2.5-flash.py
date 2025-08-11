def solve():
    """Index: 6886.
    Returns: the total number of caps made over four weeks.
    """
    # L1
    caps_week1 = 320 # 320 caps the first week
    caps_week2 = 400 # 400 the second week
    caps_week3 = 300 # 300 the third week
    total_caps_first_3_weeks = caps_week1 + caps_week2 + caps_week3

    # L2
    num_weeks = 3 # first 3 weeks
    average_caps_per_week = total_caps_first_3_weeks / num_weeks

    # L3
    total_caps_four_weeks = total_caps_first_3_weeks + average_caps_per_week

    # FA
    answer = total_caps_four_weeks
    return answer