def solve():
    """Index: 5128.
    Returns: the profit gained from the ad.
    """
    # L1
    total_customers_brought = 100 # 100 customers
    purchase_rate_decimal = 0.8 # 80% of those bought something
    customers_who_bought = total_customers_brought * purchase_rate_decimal

    # L2
    cost_per_item = 25 # cost $25
    revenue_from_customers = customers_who_bought * cost_per_item

    # L3
    advertising_cost = 1000 # $1000 for advertising
    profit = revenue_from_customers - advertising_cost

    # FA
    answer = profit
    return answer