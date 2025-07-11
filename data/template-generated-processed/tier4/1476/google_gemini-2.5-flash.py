def solve():
    """Index: 1476.
    Returns: the excess weight of the children to cross the bridge.
    """
    # L1
    percent_total = 100 # WK
    percent_less = 15 # 15% less than Megan
    kelly_weight_percent_of_megan_num = percent_total - percent_less

    # L2
    kelly_weight = 34 # Kelly weighs 34 kilograms
    percent_to_decimal_divisor = 100 # WK
    kelly_weight_percent_of_megan_decimal = kelly_weight_percent_of_megan_num / percent_to_decimal_divisor
    megan_weight = kelly_weight / kelly_weight_percent_of_megan_decimal

    # L3
    mike_weight_more_than_megan = 5 # 5 kilograms more than Megan
    mike_weight = megan_weight + mike_weight_more_than_megan

    # L4
    total_children_weight = kelly_weight + megan_weight + mike_weight

    # L5
    bridge_capacity = 100 # can hold up to 100 kilograms
    excess_weight = total_children_weight - bridge_capacity

    # FA
    answer = excess_weight
    return answer