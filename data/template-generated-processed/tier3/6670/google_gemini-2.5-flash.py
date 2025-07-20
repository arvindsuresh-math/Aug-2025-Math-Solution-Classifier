def solve():
    """Index: 6670.
    Returns: the number of green chips in the jar.
    """
    # L1
    blue_percentage = 10 # 10% of the entire chips
    white_percentage = 50 # 50% of the chips are white
    non_green_percentage = blue_percentage + white_percentage

    # L2
    total_percentage = 100 # WK
    green_percentage = total_percentage - non_green_percentage

    # L3
    num_sets_of_blue_percentage = green_percentage / blue_percentage

    # L4
    blue_chips_count = 3 # Three blue chips
    green_chips_count = blue_chips_count * num_sets_of_blue_percentage

    # FA
    answer = green_chips_count
    return answer