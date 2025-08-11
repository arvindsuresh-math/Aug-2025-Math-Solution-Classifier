def solve():
    """Index: 748.
    Returns: the amount of Scarlet's savings left after her purchases.
    """
    # L1
    earrings_cost = 23 # earrings that cost $23
    necklace_cost = 48 # necklace that cost $48
    total_spent = earrings_cost + necklace_cost

    # L2
    initial_savings = 80 # saved $80 to spend on jewelry
    savings_left = initial_savings - total_spent

    # FA
    answer = savings_left
    return answer