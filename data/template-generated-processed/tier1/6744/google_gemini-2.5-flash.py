def solve():
    """Index: 6744.
    Returns: the number of kilograms of cherries Genevieve bought.
    """
    # L1
    genevieve_had_money = 1600 # Genevieve had $1600 on her
    clarice_chipped_in = 400 # Clarice chipped in
    total_cost_cherries = genevieve_had_money + clarice_chipped_in

    # L2
    cost_per_kilogram = 8 # $8 per kilogram
    kilograms_cherries = total_cost_cherries / cost_per_kilogram

    # FA
    answer = kilograms_cherries
    return answer