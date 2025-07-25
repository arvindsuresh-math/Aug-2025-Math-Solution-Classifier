def solve(
    movie_creation_cost: int = 2000,  # He creates a movie for $2000
    dvd_cost: int = 6,  # Each DVD cost $6 to make
    dvd_price_multiplier: float = 2.5,  # He sells it for 2.5 times that much
    dvds_sold_per_day: int = 500,  # He sells 500 movies a day
    days_per_week: int = 5,  # for 5 days a week
    num_weeks: int = 20  # How much profit does he make in 20 weeks
):
    """Index: 15.
    Returns: the total profit James makes in 20 weeks.
    """

    #: L1
    dvd_selling_price = dvd_cost * dvd_price_multiplier

    #: L2
    profit_per_dvd = dvd_selling_price - dvd_cost

    #: L3
    daily_profit = profit_per_dvd * dvds_sold_per_day

    #: L4
    weekly_profit = daily_profit * days_per_week

    #: L5
    total_profit_before_movie_cost = weekly_profit * num_weeks

    #: L6

    #: FA
    answer = days_per_week
    return answer