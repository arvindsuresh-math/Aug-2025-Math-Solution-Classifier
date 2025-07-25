def solve():
    """Index: 748.
    Returns: the amount of savings Scarlet has left.
    """
    # L1
    earrings_cost = 23 # bought a pair of earrings that cost $23
    necklace_cost = 48 # bought a necklace that cost $48
    total_spent = earrings_cost + necklace_cost

    # L2
    initial_savings = 80 # saved $80
    remaining_savings = initial_savings - total_spent

    # FA
    answer = remaining_savings
    return answer