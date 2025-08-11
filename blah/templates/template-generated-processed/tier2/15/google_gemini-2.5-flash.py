def solve():
    """Index: 15.
    Returns: the total profit James makes from his media empire.
    """
    # L1
    dvd_cost_to_make = 6 # Each DVD cost $6 to make
    selling_price_multiplier = 2.5 # sells it for 2.5 times that much
    dvd_selling_price = dvd_cost_to_make * selling_price_multiplier

    # L2
    profit_per_dvd = dvd_selling_price - dvd_cost_to_make

    # L3
    movies_sold_per_day = 500 # sells 500 movies a day
    daily_profit = profit_per_dvd * movies_sold_per_day

    # L4
    days_per_week = 5 # for 5 days a week
    weekly_profit = daily_profit * days_per_week

    # L5
    num_weeks = 20 # in 20 weeks
    total_profit_from_sales = weekly_profit * num_weeks

    # L6
    movie_creation_cost = 2000 # creates a movie for $2000
    final_profit = total_profit_from_sales - movie_creation_cost

    # FA
    answer = final_profit
    return answer