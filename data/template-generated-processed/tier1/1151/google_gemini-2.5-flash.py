def solve():
    """Index: 1151.
    Returns: the total number of fried chicken pieces Pau will have eaten.
    """
    # L1
    kobe_chicken_pieces = 5 # Kobe ordered five pieces of fried chicken
    pau_order_multiplier = 2 # Pau ordered twice as much fried chicken as Kobe did
    pau_initial_order = kobe_chicken_pieces * pau_order_multiplier

    # L2
    additional_set_factor = 2 # order another set of fried chicken
    pau_total_eaten = pau_initial_order * additional_set_factor

    # FA
    answer = pau_total_eaten
    return answer