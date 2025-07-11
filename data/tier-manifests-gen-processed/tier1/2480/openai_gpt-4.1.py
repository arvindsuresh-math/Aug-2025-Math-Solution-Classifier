def solve():
    """Index: 2480.
    Returns: the total amount the school will spend on robes.
    """
    # L1
    total_singers = 30 # 30 singers
    current_robes = 12 # currently, the school has only 12 robes
    robes_to_buy = total_singers - current_robes

    # L2
    cost_per_robe = 2 # each robe costs $2
    total_cost = robes_to_buy * cost_per_robe

    # FA
    answer = total_cost
    return answer