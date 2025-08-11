def solve():
    """Index: 745.
    Returns: the total monthly sales in dollars from lettuce and tomatoes.
    """
    # L1
    lettuce_count = 2 # 2 heads of lettuce
    lettuce_price = 1 # $1 each
    lettuce_total = lettuce_count * lettuce_price

    # L2
    tomato_count = 4 # 4 tomatoes
    tomato_price = 0.5 # $0.5 apiece
    tomato_total = tomato_count * tomato_price

    # L3
    per_customer_total = lettuce_total + tomato_total

    # L4
    num_customers = 500 # 500 customers per month
    total_sales = per_customer_total * num_customers

    # FA
    answer = total_sales
    return answer