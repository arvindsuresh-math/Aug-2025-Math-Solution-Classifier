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
    dvd_selling_price = dvd_cost * dvd_selling_price_multiplier # eval: 15.0 = 6 * 2.5

    #: L2
    profit_per_dvd = dvd_selling_price - dvd_cost # eval: 9.0 = 15.0 - 6

    #: L3
    daily_profit = profit_per_dvd * movies_sold_per_day # eval: 4500.0 = 9.0 * 500

    #: L4
    weekly_profit = daily_profit * days_per_week # eval: 22500.0 = 4500.0 * 5

    #: L5
    total_profit_from_dvds = weekly_profit * num_weeks # eval: 450000.0 = 22500.0 * 20

    #: L6
    total_profit = total_profit_from_dvds - movie_creation_cost # eval: 448000.0 = 450000.0 - 2000

    #: FA
    answer = total_profit # eval: 448000.0 = 448000.0
    return answer # eval: return 448000.0
