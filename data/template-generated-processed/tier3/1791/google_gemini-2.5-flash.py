def solve():
    """Index: 1791.
    Returns: the number of delegates not wearing name badges.
    """
    # L1
    total_delegates = 36 # 16 of 36 delegates
    pre_printed_badges = 16 # 16 of 36 delegates arrived with pre-printed name badges
    delegates_without_pre_printed = total_delegates - pre_printed_badges

    # L2
    half_divisor = 2 # Half of the remaining delegates
    hand_written_badges = delegates_without_pre_printed / half_divisor

    # L3
    no_name_badge = delegates_without_pre_printed - hand_written_badges

    # FA
    answer = no_name_badge
    return answer