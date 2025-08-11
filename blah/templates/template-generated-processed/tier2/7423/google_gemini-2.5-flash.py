def solve():
    """Index: 7423.
    Returns: David's profit from selling the rice.
    """
    # L1
    price_per_kg = 1.20 # $1.20 per kilogram
    rice_weight_kg = 50 # 50 kilograms
    revenue = price_per_kg * rice_weight_kg

    # L2
    cost_of_sack = 50 # costs $50
    profit = revenue - cost_of_sack

    # FA
    answer = profit
    return answer