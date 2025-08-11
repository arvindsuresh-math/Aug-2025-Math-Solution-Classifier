def solve():
    """Index: 2387.
    Returns: the total profit Dirk made after costs and faire fee.
    """
    # L1
    num_days = 2 # sells for 2 days
    amulets_per_day = 25 # each day he sells 25 amulets
    total_amulets_sold = num_days * amulets_per_day

    # L2
    price_per_amulet = 40 # each amulet sells for 40 dollars
    total_revenue = price_per_amulet * total_amulets_sold

    # L3
    faire_fee_percent = 0.1 # has to give 10% of his revenue
    faire_fee = total_revenue * faire_fee_percent

    # L4
    revenue_after_faire = total_revenue - faire_fee

    # L5
    cost_per_amulet = 30 # they cost him 30 dollars to make
    total_cost = total_amulets_sold * cost_per_amulet

    # L6
    profit = revenue_after_faire - total_cost

    # FA
    answer = profit
    return answer