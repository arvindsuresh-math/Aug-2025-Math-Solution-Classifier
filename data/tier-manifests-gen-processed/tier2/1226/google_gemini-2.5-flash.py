def solve():
    """Index: 1226.
    Returns: the total money Nina made over the weekend.
    """
    # L1
    num_necklaces = 5 # sold 5 necklaces
    price_per_necklace = 25.00 # charges $25.00 for her necklaces
    total_necklace_sales = num_necklaces * price_per_necklace

    # L2
    num_bracelets = 10 # sold 10 bracelets
    price_per_bracelet = 15.00 # $15.00 for bracelets
    total_bracelet_sales = num_bracelets * price_per_bracelet

    # L3
    num_earrings = 20 # sold 20 earrings
    price_per_earring_pair = 10.00 # $10.00 for a pair of earrings
    total_earring_sales = num_earrings * price_per_earring_pair

    # L4
    num_ensembles = 2 # received 2 orders for a complete jewelry ensemble
    price_per_ensemble = 45.00 # Nina charged $45.00 for
    total_ensemble_sales = num_ensembles * price_per_ensemble

    # L5
    total_money_made = total_necklace_sales + total_bracelet_sales + total_earring_sales + total_ensemble_sales

    # FA
    answer = total_money_made
    return answer