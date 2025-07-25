def solve():
    """Index: 4243.
    Returns: the total amount the king paid after the tip.
    """
    # L1
    crown_cost = 20000 # costs $20,000
    tip_rate = 0.1 # tips the person 10%
    tip_amount = crown_cost * tip_rate

    # L2
    total_cost = tip_amount + crown_cost

    # FA
    answer = total_cost
    return answer