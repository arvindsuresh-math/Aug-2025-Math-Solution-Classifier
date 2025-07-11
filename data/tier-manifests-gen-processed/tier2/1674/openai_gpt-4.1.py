def solve():
    """Index: 1674.
    Returns: the total amount John spends on silver and gold.
    """
    # L1
    silver_ounces = 1.5 # John buys 1.5 ounces of silver
    silver_price_per_ounce = 20 # silver costs $20 per ounce
    silver_total = silver_ounces * silver_price_per_ounce

    # L2
    gold_multiplier = 2 # twice as much gold
    gold_ounces = silver_ounces * gold_multiplier

    # L3
    gold_price_multiplier = 50 # gold is 50 times more expensive per ounce
    gold_price_per_ounce = silver_price_per_ounce * gold_price_multiplier

    # L4
    gold_total = gold_ounces * gold_price_per_ounce

    # L5
    total_spent = silver_total + gold_total

    # FA
    answer = total_spent
    return answer