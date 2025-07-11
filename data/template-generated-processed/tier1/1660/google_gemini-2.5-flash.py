def solve():
    """Index: 1660.
    Returns: the number of green papayas left on the tree.
    """
    # L1
    friday_yellow = 2 # two of the fruits turned yellow
    multiplier_sunday = 2 # twice as many fruits as on Friday
    sunday_yellow = friday_yellow * multiplier_sunday

    # L2
    total_yellow = friday_yellow + sunday_yellow

    # L3
    initial_green_papayas = 14 # 14 green papayas
    remaining_green = initial_green_papayas - total_yellow

    # FA
    answer = remaining_green
    return answer