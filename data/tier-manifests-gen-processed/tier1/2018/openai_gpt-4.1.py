def solve():
    """Index: 2018.
    Returns: Jessica's total monthly payment if she adds movie and sports channels.
    """
    # L1
    movie_channels_cost = 12 # movie channels, it will cost an additional $12 per month
    sports_channels_less = 3 # sports channels cost $3 less per month than the movie channels
    sports_channels_cost = movie_channels_cost - sports_channels_less

    # L2
    basic_cable_cost = 15 # basic cable television service for $15 per month
    total_monthly_payment = basic_cable_cost + movie_channels_cost + sports_channels_cost

    # FA
    answer = total_monthly_payment
    return answer