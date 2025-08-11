def solve():
    """Index: 5364.
    Returns: Jenna's total profit or loss for the month.
    """
    # L1
    worker_salary = 2500 # $2,500 each
    num_workers = 4 # four workers
    salaries_cost = worker_salary * num_workers

    # L2
    monthly_rent = 10000 # $10,000 in rent
    total_fixed_costs = salaries_cost + monthly_rent

    # L3
    resale_price = 8 # resells it for $8
    widget_cost = 3 # pays $3 for each widget
    profit_per_widget = resale_price - widget_cost

    # L4
    widgets_sold = 5000 # sells 5000 widgets
    gross_profit_from_sales = profit_per_widget * widgets_sold

    # L5
    profit_before_taxes = gross_profit_from_sales - total_fixed_costs

    # L6
    tax_rate_percent = 20 # 20% of her total profit in taxes
    tax_rate_decimal = 0.2 # 20% of her total profit in taxes
    taxes_owed = profit_before_taxes * tax_rate_decimal

    # L7
    total_profit = profit_before_taxes - taxes_owed

    # FA
    answer = total_profit
    return answer