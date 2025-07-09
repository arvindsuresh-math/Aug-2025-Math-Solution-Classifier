def solve(
    movie_creation_cost: int = 2000, # James creates a movie for $2000
    dvd_cost: int = 6, # Each DVD cost $6 to make
    dvd_selling_price_multiplier: float = 2.5, # He sells it for 2.5 times that much
    movies_sold_per_day: int = 500, # He sells 500 movies a day
    days_per_week: int = 5, # for 5 days a week
    num_weeks: int = 20 # in 20 weeks
):
    """Index: 15.
    Returns: the total profit James makes in 20 weeks.
    """

    #: L1
    dvd_selling_price = days_per_week * dvd_selling_price_multiplier # eval: 12.5 = 5 * 2.5

    #: L2
    profit_per_dvd = dvd_selling_price - dvd_cost # eval: 6.5 = 12.5 - 6

    #: L3
    daily_profit = profit_per_dvd * movies_sold_per_day # eval: 3250.0 = 6.5 * 500

    #: L4
    weekly_profit = daily_profit * days_per_week # eval: 16250.0 = 3250.0 * 5

    #: L5
    total_profit_from_dvds = weekly_profit * num_weeks # eval: 325000.0 = 16250.0 * 20

    #: L6
    total_profit = total_profit_from_dvds - movie_creation_cost # eval: 323000.0 = 325000.0 - 2000

    #: FA
    answer = total_profit
    return answer # eval: return 323000.0
