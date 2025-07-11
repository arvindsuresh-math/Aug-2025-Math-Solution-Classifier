def solve():
    """Index: 2392.
    Returns: the total profit John makes a month.
    """
    # L1
    sales_multiplier = 1.4 # sells the computers for 1.4 times the value
    parts_cost_per_computer = 800 # The parts for the computer cost $800
    selling_price_per_computer = sales_multiplier * parts_cost_per_computer

    # L2
    profit_per_computer = selling_price_per_computer - parts_cost_per_computer

    # L3
    computers_per_month = 60 # build 60 computers a month
    total_profit_from_sales = profit_per_computer * computers_per_month

    # L4
    rent_expense = 5000 # pay $5000 a month in rent
    other_expenses = 3000 # another $3000 in non-rent extra expenses a month
    total_monthly_expenses = rent_expense + other_expenses

    # L5
    monthly_profit = total_profit_from_sales - total_monthly_expenses

    # FA
    answer = monthly_profit
    return answer