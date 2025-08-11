def solve():
    """Index: 5260.
    Returns: the amount of money Celia is going to put into her savings account.
    """
    # L1
    food_budget_per_week = 100 # $100 a week on food
    num_weeks = 4 # next 4 weeks
    monthly_food_cost = food_budget_per_week * num_weeks

    # L2
    rent_cost = 1500 # $1500
    streaming_cost = 30 # $30 set aside for video streaming services
    cell_phone_cost = 50 # $50 planned for one month of cell phone usage
    total_fixed_monthly_costs = rent_cost + streaming_cost + cell_phone_cost

    # L3
    savings_percent_text = 10 # 10% of it to put into savings
    total_monthly_spending = monthly_food_cost + total_fixed_monthly_costs

    # L4
    savings_percent_decimal = 0.10 # from solution text: .10 x 1980
    savings_amount = savings_percent_decimal * total_monthly_spending

    # FA
    answer = savings_amount
    return answer