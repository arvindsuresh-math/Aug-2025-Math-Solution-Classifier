def solve():
    """Index: 1226.
    Returns: the total amount of money Nina made over the weekend.
    """
    # L1
    num_necklaces = 5 # sold 5 necklaces
    price_necklace = 25.00 # charges $25.00 for her necklaces
    total_necklaces = num_necklaces * price_necklace

    # L2
    num_bracelets = 10 # sold 10 bracelets
    price_bracelet = 15.00 # $15.00 for bracelets
    total_bracelets = num_bracelets * price_bracelet

    # L3
    num_earrings = 20 # sold 20 earrings
    price_earrings = 10.00 # $10.00 for a pair of earrings
    total_earrings = num_earrings * price_earrings

    # L4
    num_ensembles = 2 # 2 orders for a complete jewelry ensemble
    price_ensemble = 45.00 # charged $45.00 for ensemble
    total_ensembles = num_ensembles * price_ensemble

    # L5
    total_money = total_necklaces + total_bracelets + total_earrings + total_ensembles

    # FA
    answer = total_money
    return answer