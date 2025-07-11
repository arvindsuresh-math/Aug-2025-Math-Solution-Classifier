def solve():
    """Index: 15.
    Returns: the total profit James makes in 20 weeks after accounting for the movie creation cost.
    """
    # L1
    dvd_cost = 6 # Each DVD cost $6 to make
    sell_multiplier = 2.5 # Sells it for 2.5 times that much
    sell_price = dvd_cost * sell_multiplier

    # L2
    profit_per_dvd = sell_price - dvd_cost

    # L3
    dvds_per_day = 500 # Sells 500 movies a day
    daily_profit = profit_per_dvd * dvds_per_day

    # L4
    days_per_week = 5 # 5 days a week
    weekly_profit = daily_profit * days_per_week

    # L5
    num_weeks = 20 # in 20 weeks
    total_profit_before_movie = weekly_profit * num_weeks

    # L6
    movie_cost = 2000 # creates a movie for $2000
    final_profit = total_profit_before_movie - movie_cost

    # FA
    answer = final_profit
    return answer