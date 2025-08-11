def solve():
    """Index: 7438.
    Returns: how much more money Logan must make each year.
    """
    # L1
    rent_cost = 20000 # $20,000 on rent every year
    groceries_cost = 5000 # $5000 on groceries every year
    gas_cost = 8000 # $8000 on gas every year
    total_spending = rent_cost + groceries_cost + gas_cost

    # L2
    annual_income = 65000 # $65,000 a year
    money_left_after_spending = annual_income - total_spending

    # L3
    desired_money_left = 42000 # at least $42000 left
    additional_money_needed = desired_money_left - money_left_after_spending

    # FA
    answer = additional_money_needed
    return answer