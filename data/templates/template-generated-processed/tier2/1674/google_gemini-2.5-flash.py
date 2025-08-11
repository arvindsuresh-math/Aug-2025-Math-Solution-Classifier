def solve():
    """Index: 1674.
    Returns: the total amount John spends on silver and gold.
    """
    # L1
    silver_ounces = 1.5 # 1.5 ounces of silver
    silver_cost_per_ounce = 20 # $20 per ounce
    total_silver_cost = silver_ounces * silver_cost_per_ounce

    # L2
    gold_multiplier = 2 # twice as much gold
    gold_ounces = silver_ounces * gold_multiplier

    # L3
    gold_price_multiplier = 50 # 50 times more expensive
    gold_cost_per_ounce = silver_cost_per_ounce * gold_price_multiplier

    # L4
    total_gold_cost = gold_ounces * gold_cost_per_ounce

    # L5
    total_spent = total_silver_cost + total_gold_cost

    # FA
    answer = total_spent
    return answer