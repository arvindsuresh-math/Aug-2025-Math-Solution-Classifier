def solve(
        movie_creation_cost: int = 2000,  # He creates a movie for $2000
        dvd_production_cost: int = 6,  # Each DVD cost $6 to make
        markup_multiplier: float = 2.5,  # He sells it for 2.5 times that much
        daily_sales: int = 500,  # He sells 500 movies a day
        days_per_week: int = 5,  # for 5 days a week
        total_weeks: int = 20  # How much profit does he make in 20 weeks
    ):
    """Index: 15.
    Returns: the total profit James makes from selling DVDs over 20 weeks.
    """

    #: L1
    selling_price = dvd_production_cost * markup_multiplier # eval: 15.0 = 6 * 2.5

    #: L2
    profit_per_dvd = selling_price - dvd_production_cost # eval: 9.0 = 15.0 - 6

    #: L3
    daily_profit = profit_per_dvd * daily_sales # eval: 4500.0 = 9.0 * 500

    #: L4
    weekly_profit = daily_profit * days_per_week # eval: 22500.0 = 4500.0 * 5

    #: L5
    total_revenue = weekly_profit * total_weeks # eval: 450000.0 = 22500.0 * 20

    #: L6
    final_profit = total_revenue - movie_creation_cost # eval: 448000.0 = 450000.0 - 2000

    #: FA
    answer = final_profit
    return answer # eval: return 448000.0
