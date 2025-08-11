def solve():
    """Index: 1376.
    Returns: the number of yellow leaves Bronson collects.
    """
    # L1
    thursday_leaves = 12 # collects 12 on Thursday
    friday_leaves = 13 # collects 13 on Friday
    total_leaves = thursday_leaves + friday_leaves

    # L2
    percent_total = 100 # WK (percentages sum to 100)
    percent_brown = 20 # 20% are Brown
    percent_green = 20 # 20% are Green
    percent_yellow = percent_total - percent_brown - percent_green

    # L3
    percent_yellow_decimal = 0.6 # 60% as decimal
    yellow_leaves = total_leaves * percent_yellow_decimal

    # FA
    answer = yellow_leaves
    return answer