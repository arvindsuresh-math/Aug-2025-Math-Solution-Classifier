def solve():
    """Index: 5695.
    Returns: the percentage of chips Lyle had.
    """
    # L1
    ian_ratio_part = 4 # in the ratio 4:6
    lyle_ratio_part = 6 # in the ratio 4:6
    total_ratio_parts = ian_ratio_part + lyle_ratio_part

    # L2
    total_chips = 100 # One hundred chips
    chips_per_part = total_chips / total_ratio_parts

    # L3
    lyle_chips = lyle_ratio_part * chips_per_part

    # L4
    percentage_multiplier = 100 # for converting to percentage
    lyle_percentage = (lyle_chips / total_chips) * percentage_multiplier

    # FA
    answer = lyle_percentage
    return answer