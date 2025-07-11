def solve():
    """Index: 487.
    Returns: the profit Jonah made from selling pineapple rings.
    """
    # L1
    pineapples_bought = 6 # Jonah bought 6 pineapples
    price_per_pineapple = 3 # $3 each
    total_spent = pineapples_bought * price_per_pineapple

    # L2
    rings_per_pineapple = 12 # Each pineapple could be cut into 12 rings
    total_rings = pineapples_bought * rings_per_pineapple

    # L3
    rings_per_set = 4 # He sold 4 pineapple rings for $5 each
    sets_sold = total_rings / rings_per_set

    # L4
    price_per_set = 5 # $5 each set
    total_earned = sets_sold * price_per_set

    # L5
    profit = total_earned - total_spent

    # FA
    answer = profit
    return answer