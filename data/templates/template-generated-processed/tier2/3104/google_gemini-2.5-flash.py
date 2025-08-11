def solve():
    """Index: 3104.
    Returns: the amount Mark should add for the tip.
    """
    # L1
    tip_percentage_num = 20 # 20%
    check_amount = 200 # $200 check
    percent_factor = 0.01 # WK
    total_tip_amount = tip_percentage_num * percent_factor * check_amount

    # L2
    friend_contribution = 10 # kick in $10
    mark_contribution = total_tip_amount - friend_contribution

    # FA
    answer = mark_contribution
    return answer