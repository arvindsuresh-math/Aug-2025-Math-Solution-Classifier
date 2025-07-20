def solve():
    """Index: 5439.
    Returns: the total money raised for charity.
    """
    # L1
    num_regular_ducks = 221 # 221 regular size ducks
    price_regular_duck = 3.00 # $3.00 each
    revenue_regular_ducks = num_regular_ducks * price_regular_duck

    # L2
    num_large_ducks = 185 # 185 large size ducks
    price_large_duck = 5.00 # $5.00 each
    revenue_large_ducks = num_large_ducks * price_large_duck

    # L3
    total_revenue = revenue_regular_ducks + revenue_large_ducks

    # FA
    answer = total_revenue
    return answer