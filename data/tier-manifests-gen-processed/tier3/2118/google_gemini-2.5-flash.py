def solve():
    """Index: 2118.
    Returns: the number of businesses Brandon can still apply to.
    """
    # L1
    total_businesses = 72 # 72 business in town
    fired_divisor = 2 # half the businesses
    not_fired_from = total_businesses / fired_divisor

    # L2
    quit_divisor = 3 # a third of them
    quit_from = total_businesses / quit_divisor

    # L3
    can_still_apply_to = not_fired_from - quit_from

    # FA
    answer = can_still_apply_to
    return answer