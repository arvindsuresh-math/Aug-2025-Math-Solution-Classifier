def solve():
    """Index: 1645.
    Returns: the amount of change Raine gets back.
    """
    # L1
    num_bracelets = 3 # three bracelets
    cost_bracelet = 15 # bracelets at $15 each
    cost_bracelets_total = num_bracelets * cost_bracelet

    # L2
    num_necklaces = 2 # two gold heart necklaces
    cost_necklace = 10 # a gold heart necklace at $10
    cost_necklaces_total = num_necklaces * cost_necklace

    # L3
    cost_coffee_mug = 20 # a personalized coffee mug at $20
    total_cost_items = cost_bracelets_total + cost_necklaces_total + cost_coffee_mug

    # L4
    amount_given = 100 # a one hundred dollar bill
    change_back = amount_given - total_cost_items

    # FA
    answer = change_back
    return answer