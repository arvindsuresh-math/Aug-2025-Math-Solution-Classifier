def solve():
    """Index: 7086.
    Returns: the total earnings of the booth after paying rent and ingredients.
    """
    # L1
    popcorn_daily_sales = 50 # $50 selling popcorn each day
    cotton_candy_multiplier = 3 # three times as much selling cotton candy
    cotton_candy_daily_sales = popcorn_daily_sales * cotton_candy_multiplier

    # L2
    total_daily_sales = cotton_candy_daily_sales + popcorn_daily_sales

    # L3
    activity_days = 5 # For a 5-day activity
    total_sales_5_days = total_daily_sales * activity_days

    # L4
    rent_cost = 30 # $30 rent
    ingredients_cost = 75 # $75 for the cost of the ingredients
    total_expenses = rent_cost + ingredients_cost

    # L5
    net_earnings = total_sales_5_days - total_expenses

    # FA
    answer = net_earnings
    return answer