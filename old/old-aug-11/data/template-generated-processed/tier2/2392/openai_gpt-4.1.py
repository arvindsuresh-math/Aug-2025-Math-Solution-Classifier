def solve():
    """Index: 2392.
    Returns: the monthly profit John makes from his computer business.
    """
    # L1
    markup_multiplier = 1.4 # sells the computers for 1.4 times the value
    component_cost = 800 # parts for the computer cost $800
    sale_price = markup_multiplier * component_cost

    # L2
    profit_per_computer = sale_price - component_cost

    # L3
    computers_per_month = 60 # build 60 computers a month
    total_computer_profit = profit_per_computer * computers_per_month

    # L4
    rent_expense = 5000 # $5000 a month in rent
    extra_expenses = 3000 # $3000 in non-rent extra expenses
    total_expenses = rent_expense + extra_expenses

    # L5
    monthly_profit = total_computer_profit - total_expenses

    # FA
    answer = monthly_profit
    return answer