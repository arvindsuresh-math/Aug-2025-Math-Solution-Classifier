def solve():
    """Index: 5027.
    Returns: the amount of money Collin would have to put into savings.
    """
    # L1
    cans_at_home = 12 # 12 cans at home
    grandparents_multiplier = 3 # three times as many
    cans_from_grandparents = cans_at_home * grandparents_multiplier

    # L2
    cans_from_neighbor = 46 # His neighbor gave him 46
    cans_from_dad = 250 # His dad brought home 250 cans from the office
    total_cans_collected = cans_at_home + cans_from_grandparents + cans_from_neighbor + cans_from_dad

    # L3
    value_per_can = 0.25 # $0.25 per aluminum can
    total_money_earned = value_per_can * total_cans_collected

    # L4
    savings_divisor = 2 # half of his entire amount collected
    money_to_savings = total_money_earned / savings_divisor

    # FA
    answer = money_to_savings
    return answer