def solve():
    """Index: 5347.
    Returns: the total amount the shop earned.
    """
    # L1
    cola_bottles_sold = 15 # 15 bottles of cola
    cola_cost_per_bottle = 3 # costs $3
    cola_total_cost = cola_bottles_sold * cola_cost_per_bottle

    # L2
    juice_bottles_sold = 12 # 12 bottles of juice
    juice_cost_per_bottle = 1.5 # juice for $1.5
    juice_total_cost = juice_bottles_sold * juice_cost_per_bottle

    # L3
    water_bottles_sold = 25 # 25 bottles of water
    water_cost_per_bottle = 1 # water for $1 per bottle
    water_total_cost = water_bottles_sold * water_cost_per_bottle
    total_earnings = cola_total_cost + juice_total_cost + water_total_cost

    # FA
    answer = total_earnings
    return answer