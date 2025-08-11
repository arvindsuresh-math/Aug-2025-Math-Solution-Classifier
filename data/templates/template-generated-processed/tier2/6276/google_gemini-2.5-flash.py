def solve():
    """Index: 6276.
    Returns: the number of pounds of garbage Zane picked up.
    """
    # L1
    daliah_pounds = 17.5 # Daliah picked up 17.5 pounds of garbage

    # L2
    less_than_daliah = 2 # 2 pounds less than Daliah
    dewei_pounds = daliah_pounds - less_than_daliah

    # L3
    zane_multiplier = 4 # 4 times as many pounds of garbage as Dewei
    zane_pounds = zane_multiplier * dewei_pounds

    # FA
    answer = zane_pounds
    return answer