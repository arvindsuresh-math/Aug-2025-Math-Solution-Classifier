def solve():
    """Index: 1269.
    Returns: the total revenue for the day.
    """
    # L1
    federal_return_cost = 50 # $50 for a federal return
    federal_returns_sold = 60 # 60 federal returns
    federal_income = federal_return_cost * federal_returns_sold

    # L2
    state_return_cost = 30 # $30 for a state return
    state_returns_sold = 20 # 20 state returns
    state_income = state_return_cost * state_returns_sold

    # L3
    quarterly_tax_cost = 80 # $80 for quarterly business taxes
    quarterly_returns_sold = 10 # 10 quarterly returns
    quarterly_income = quarterly_tax_cost * quarterly_returns_sold

    # L4
    total_revenue = federal_income + state_income + quarterly_income

    # FA
    answer = total_revenue
    return answer