def solve():
    """Index: 5870.
    Returns: the total money Keaton can earn every year.
    """
    # L1
    months_per_year = 12 # WK
    orange_harvest_interval_months = 2 # every 2 months
    orange_harvest_times_per_year = months_per_year / orange_harvest_interval_months

    # L2
    orange_harvest_value = 50 # for $50
    total_orange_earnings_per_year = orange_harvest_value * orange_harvest_times_per_year

    # L3
    apple_harvest_interval_months = 3 # every 3 months
    apple_harvest_times_per_year = months_per_year / apple_harvest_interval_months

    # L4
    apple_harvest_value = 30 # for $30
    total_apple_earnings_per_year = apple_harvest_value * apple_harvest_times_per_year

    # L5
    total_annual_earnings = total_orange_earnings_per_year + total_apple_earnings_per_year

    # FA
    answer = total_annual_earnings
    return answer