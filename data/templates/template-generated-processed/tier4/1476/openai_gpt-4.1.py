def solve():
    """Index: 1476.
    Returns: the amount (in kg) by which the three children exceed the bridge's weight limit.
    """
    # L1
    kelly_weight = 34 # Kelly weighs 34 kilograms
    percent_100 = 100 # WK
    kelly_less_percent = 15 # 15% less than Megan
    megan_percent = percent_100 - kelly_less_percent

    # L2
    megan_percent_decimal = 0.85 # 85% is 0.85
    megan_weight = kelly_weight / megan_percent_decimal

    # L3
    mike_more_than_megan = 5 # Mike weighs 5 kilograms more than Megan
    mike_weight = megan_weight + mike_more_than_megan

    # L4
    total_weight = kelly_weight + megan_weight + mike_weight

    # L5
    bridge_limit = 100 # can hold up to 100 kilograms at once
    excess_weight = total_weight - bridge_limit

    # FA
    answer = excess_weight
    return answer