def solve():
    """Index: 4608.
    Returns: the total number of drums hit.
    """
    # L1
    entry_cost = 10 # It costs $10 to enter
    money_lost = 7.5 # lost $7.5 for joining the contest
    money_made_from_drums = entry_cost - money_lost

    # L3
    cents_per_drum = 2.5 # 2.5 cents for every drum hit
    dollars_per_cent = 0.01 # WK
    value_per_drum_dollar = cents_per_drum * dollars_per_cent
    drums_for_money_made = money_made_from_drums / value_per_drum_dollar

    # L4
    threshold_drums = 200 # If she hits 200 drums, she can start to make money
    total_drums_hit = drums_for_money_made + threshold_drums

    # FA
    answer = total_drums_hit
    return answer