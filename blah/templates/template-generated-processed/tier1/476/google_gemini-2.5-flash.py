def solve():
    """Index: 476.
    Returns: the cost of the High Jump sneakers.
    """
    # L1
    num_lawns = 3 # mow 3 neighbors’ lawns
    price_per_lawn = 8 # $8 a lawn
    earnings_lawns = num_lawns * price_per_lawn

    # L2
    num_figures = 2 # sell 2 collectible figures
    price_per_figure = 9 # $9 each
    earnings_figures = num_figures * price_per_figure

    # L3
    hours_worked = 10 # work an after-school job for 10 hours
    hourly_rate = 5 # $5 per hour
    earnings_job = hours_worked * hourly_rate

    # L4
    total_cost_sneakers = earnings_lawns + earnings_figures + earnings_job

    # FA
    answer = total_cost_sneakers
    return answer