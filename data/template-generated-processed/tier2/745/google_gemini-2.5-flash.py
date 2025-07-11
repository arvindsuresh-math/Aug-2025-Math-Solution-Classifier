def solve():
    """Index: 745.
    Returns: the total money the store will receive in sales of lettuce and tomatoes per month.
    """
    # L1
    lettuce_heads = 2 # 2 heads of lettuce
    lettuce_price_per_head = 1 # $1 each
    lettuce_cost_per_customer = lettuce_heads * lettuce_price_per_head

    # L2
    tomato_count = 4 # 4 tomatoes
    tomato_price_apiece = 0.5 # $0.5 apiece
    tomato_cost_per_customer = tomato_count * tomato_price_apiece

    # L3
    total_cost_per_customer = lettuce_cost_per_customer + tomato_cost_per_customer

    # L4
    num_customers_per_month = 500 # 500 customers per month
    total_monthly_sales = total_cost_per_customer * num_customers_per_month

    # FA
    answer = total_monthly_sales
    return answer