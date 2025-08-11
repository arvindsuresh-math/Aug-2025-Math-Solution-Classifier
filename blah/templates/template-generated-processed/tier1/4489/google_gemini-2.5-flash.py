def solve():
    """Index: 4489.
    Returns: the additional money Michael needs.
    """
    # L1
    cake_cost = 20 # a cake for $20
    bouquet_cost = 36 # a bouquet for $36
    balloons_cost = 5 # a set of balloons for $5
    total_cost = cake_cost + bouquet_cost + balloons_cost

    # L2
    michael_has = 50 # Michael has $50
    money_needed = total_cost - michael_has

    # FA
    answer = money_needed
    return answer