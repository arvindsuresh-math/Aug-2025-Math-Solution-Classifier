def solve():
    """Index: 265.
    Returns: the total height they can reach.
    """
    # L1
    larry_full_height = 5 # Larry is 5 feet tall
    shoulder_height_reduction_percent = 20 # 20% less
    shoulder_height_reduction_decimal = 0.2 # 0.2*5
    percent_factor = 0.01 # WK
    shoulder_height_reduction_amount = shoulder_height_reduction_decimal * larry_full_height

    # L2
    larry_shoulder_height = larry_full_height - shoulder_height_reduction_amount

    # L3
    barry_reach_height = 5 # Barry can reach apples that are 5 feet high
    total_reach_height = larry_shoulder_height + barry_reach_height

    # FA
    answer = total_reach_height
    return answer