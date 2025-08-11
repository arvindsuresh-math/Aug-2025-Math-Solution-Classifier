def solve():
    """Index: 2749.
    Returns: the total number of baskets made by Alex, Sandra, and Hector.
    """
    # L1
    alex_baskets = 8 # Alex made 8 baskets
    sandra_multiplier = 3 # Sandra made three times as many baskets as Alex
    sandra_baskets = sandra_multiplier * alex_baskets

    # L2
    hector_multiplier = 2 # Hector made two times the number of baskets that Sandra made
    hector_baskets = sandra_baskets * hector_multiplier

    # L3
    total_baskets = alex_baskets + sandra_baskets + hector_baskets

    # FA
    answer = total_baskets
    return answer