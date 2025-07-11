def solve():
    """Index: 2018.
    Returns: Jessica's total monthly payment if she adds movie and sports channels.
    """
    # L1
    movie_channels_cost = 12 # additional $12 per month
    sports_channels_cost_reduction = 3 # $3 less per month than the movie channels
    sports_channels_cost = movie_channels_cost - sports_channels_cost_reduction

    # L2
    basic_cable_cost = 15 # $15 per month
    total_monthly_payment = basic_cable_cost + movie_channels_cost + sports_channels_cost

    # FA
    answer = total_monthly_payment
    return answer