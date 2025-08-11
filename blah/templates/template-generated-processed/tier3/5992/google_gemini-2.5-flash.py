def solve():
    """Index: 5992.
    Returns: the number of days until the roof collapses.
    """
    # L1
    max_weight_pounds = 500 # Bill's roof can bear 500 pounds of weight
    leaves_per_pound = 1000 # 1000 leaves weighs 1 pound
    max_leaves_roof_can_hold = max_weight_pounds * leaves_per_pound

    # L2
    leaves_fall_per_day = 100 # 100 leaves fall on his roof every day
    days_to_collapse = max_leaves_roof_can_hold / leaves_fall_per_day

    # FA
    answer = days_to_collapse
    return answer