def solve():
    """Index: 476.
    Returns: the cost of the High Jump sneakers.
    """
    # L1
    lawns_mowed = 3 # mow 3 neighbors’ lawns
    pay_per_lawn = 8 # $8 a lawn
    lawn_earnings = lawns_mowed * pay_per_lawn

    # L2
    figures_sold = 2 # sell 2 collectible figures
    price_per_figure = 9 # $9 each
    figure_earnings = figures_sold * price_per_figure

    # L3
    job_hours = 10 # work 10 hours
    pay_per_hour = 5 # $5 per hour
    job_earnings = job_hours * pay_per_hour

    # L4
    sneakers_cost = lawn_earnings + figure_earnings + job_earnings

    # FA
    answer = sneakers_cost
    return answer