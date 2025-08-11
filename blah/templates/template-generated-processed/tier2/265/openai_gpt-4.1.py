def solve():
    """Index: 265.
    Returns: the maximum height Larry and Barry can reach if Barry stands on Larry's shoulders.
    """
    # L1
    larry_height = 5 # Larry is 5 feet tall
    shoulder_percent_less_num = 20 # 20% less
    percent_factor = 0.01 # WK
    shoulder_percent_less_decimal = 0.2 # 20% less
    shoulder_height_difference = shoulder_percent_less_num * percent_factor * larry_height

    # L2
    larry_shoulder_height = larry_height - shoulder_height_difference

    # L3
    barry_reach = 5 # Barry can reach apples that are 5 feet high
    combined_reach = larry_shoulder_height + barry_reach

    # FA
    answer = combined_reach
    return answer