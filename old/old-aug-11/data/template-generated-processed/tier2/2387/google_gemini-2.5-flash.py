def solve():
    """Index: 2387.
    Returns: the total profit Dirk made.
    """
    # L1
    num_days = 2 # sells for 2 days
    amulets_per_day = 25 # each day he sells 25 amulets
    total_amulets_sold = num_days * amulets_per_day

    # L2
    price_per_amulet = 40 # Each amulet sells for 40 dollars
    total_revenue = price_per_amulet * total_amulets_sold

    # L3
    faire_revenue_share_decimal = 0.1 # give 10% of his revenue
    faire_share_amount = total_revenue * faire_revenue_share_decimal

    # L4
    revenue_kept = total_revenue - faire_share_amount

    # L5
    cost_to_make_per_amulet = 30 # they cost him 30 dollars to make
    total_cost_to_make = total_amulets_sold * cost_to_make_per_amulet

    # L6
    profit = revenue_kept - total_cost_to_make

    # FA
    answer = profit
    return answer