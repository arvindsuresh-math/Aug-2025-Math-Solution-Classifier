def solve():
    """Index: 5299.
    Returns: the money Dianne keeps in sales after subtracting the returns.
    """
    # L1
    num_customers = 1000 # 1000 customers
    book_cost = 15 # 15 dollars apiece
    total_sales = num_customers * book_cost

    # L2
    return_percent_num = 37 # 37% of her 1000 customers
    return_percent_decimal = 0.37 # from solution text: .37*1000
    percent_factor = 0.01 # WK
    num_returns = return_percent_num * percent_factor * num_customers

    # L3
    total_returns_cost = num_returns * book_cost

    # L4
    final_income = total_sales - total_returns_cost

    # FA
    answer = final_income
    return answer