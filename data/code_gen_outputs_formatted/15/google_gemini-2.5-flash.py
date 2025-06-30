def solve(
        movie_creation_cost: int = 2000,  # creates a movie for $2000
        dvd_production_cost: int = 6,  # Each DVD cost $6 to make
        sales_multiplier: float = 2.5,  # He sells it for 2.5 times that much
        movies_sold_per_day: int = 500,  # He sells 500 movies a day
        selling_days_per_week: int = 5,  # for 5 days a week
        number_of_weeks: int = 20  # in 20 weeks
    ):
    """Index: 15.
    Returns: the total profit James makes in 20 weeks.
    """

    #: L1
    dvd_selling_price = dvd_production_cost * sales_multiplier

    #: L2
    profit_per_dvd = dvd_selling_price - dvd_production_cost

    #: L3
    daily_profit = profit_per_dvd * movies_sold_per_day

    #: L4
    weekly_profit = daily_profit * selling_days_per_week

    #: L5
    total_profit_from_sales = weekly_profit * number_of_weeks

    #: L6
    net_profit = total_profit_from_sales - movie_creation_cost

    #: FA
    answer = net_profit
    return answer