def solve():
    """Index: 3291.
    Returns: the amount Sally and Carl each owe in dollars.
    """
    # L1
    total_promised = 400 # promised to contribute $400
    total_received = 285 # actually received $285
    total_owed = total_promised - total_received

    # L2
    amy_owes = 30 # Amy owes $30
    half_divisor = 2 # half as much as Amy
    derek_owes = amy_owes / half_divisor

    # L3
    sally_carl_combined_owed = total_owed - amy_owes - derek_owes

    # L4
    sally_carl_each_owe = sally_carl_combined_owed / half_divisor

    # FA
    answer = sally_carl_each_owe
    return answer