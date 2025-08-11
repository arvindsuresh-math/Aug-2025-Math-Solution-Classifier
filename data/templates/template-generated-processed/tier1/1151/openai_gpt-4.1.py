def solve():
    """Index: 1151.
    Returns: the total number of pieces of fried chicken Pau will have eaten in all.
    """
    # L1
    kobe_order = 5 # Kobe ordered five pieces of fried chicken
    pau_multiplier = 2 # Pau ordered twice as much fried chicken as Kobe did
    pau_order = kobe_order * pau_multiplier

    # L2
    another_set = 2 # they order another set of fried chicken (Pau will have eaten two sets in total)
    pau_total = pau_order * another_set

    # FA
    answer = pau_total
    return answer