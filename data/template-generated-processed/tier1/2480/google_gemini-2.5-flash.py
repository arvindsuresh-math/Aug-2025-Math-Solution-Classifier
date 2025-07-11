def solve():
    """Index: 2480.
    Returns: the total amount the school will spend on robes.
    """
    # L1
    robes_needed = 30 # 30 singers
    robes_have = 12 # only 12 robes
    robes_to_buy = robes_needed - robes_have

    # L2
    cost_per_robe = 2 # $2
    total_spend = robes_to_buy * cost_per_robe

    # FA
    answer = total_spend
    return answer