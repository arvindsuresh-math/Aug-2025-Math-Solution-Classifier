def solve():
    """Index: 3383.
    Returns: the percentage of ads that aren't interesting and don't get blocked.
    """
    # L1
    total_percentage = 100 # WK
    interesting_ads_blocked_percentage = 20 # 20% of the ads it doesn't block are actually interesting
    not_interesting_percentage = total_percentage - interesting_ads_blocked_percentage

    # L2
    ads_not_blocked_percentage = 20 # all but 20% of ads
    percentage_divisor = 100 # WK
    uninteresting_unblocked_percentage = (not_interesting_percentage * ads_not_blocked_percentage) / percentage_divisor

    # FA
    answer = uninteresting_unblocked_percentage
    return answer