def solve():
    """Index: 4575.
    Returns: the total profit Laran makes per 5-day school week.
    """
    # L1
    large_poster_sell_price = 10 # sell for $10
    large_poster_cost = 5 # cost her $5 to make
    profit_per_large_poster = large_poster_sell_price - large_poster_cost

    # L2
    num_large_posters_per_day = 2 # Two posters per day are her large posters
    daily_profit_large_posters = profit_per_large_poster * num_large_posters_per_day

    # L3
    small_poster_sell_price = 6 # small posters that sell for $6
    small_poster_cost = 3 # They cost $3 to produce
    profit_per_small_poster = small_poster_sell_price - small_poster_cost

    # L4
    total_posters_per_day = 5 # selling 5 posters per day
    num_small_posters_per_day = total_posters_per_day - num_large_posters_per_day
    daily_profit_small_posters = profit_per_small_poster * num_small_posters_per_day

    # L5
    total_daily_profit = daily_profit_large_posters + daily_profit_small_posters

    # L6
    school_week_days = 5 # 5-day school week
    weekly_profit = school_week_days * total_daily_profit

    # FA
    answer = weekly_profit
    return answer