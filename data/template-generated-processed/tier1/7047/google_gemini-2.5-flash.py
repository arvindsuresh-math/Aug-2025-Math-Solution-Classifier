def solve():
    """Index: 7047.
    Returns: the total amount Iris spent on clothes.
    """
    # L1
    num_jackets = 3 # three jackets
    price_per_jacket = 10 # $10 each
    cost_jackets = num_jackets * price_per_jacket

    # L2
    num_shorts = 2 # two pairs of shorts
    price_per_short = 6 # $6 each
    cost_shorts = num_shorts * price_per_short

    # L3
    num_pants = 4 # four pairs of pants
    price_per_pant = 12 # $12 each
    cost_pants = num_pants * price_per_pant

    # L4
    total_spent = cost_jackets + cost_shorts + cost_pants

    # FA
    answer = total_spent
    return answer