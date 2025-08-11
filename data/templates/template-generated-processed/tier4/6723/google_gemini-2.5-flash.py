def solve():
    """Index: 6723.
    Returns: the number of years it took Bob to grow out his hair.
    """
    # L1
    current_length = 36 # 36 inches long
    initial_length = 6 # 6 inches
    total_growth = current_length - initial_length

    # L2
    months_per_year = 12 # WK
    monthly_growth_rate = 0.5 # .5 inches per month
    annual_growth_rate = months_per_year * monthly_growth_rate

    # L3
    time_in_years = total_growth / annual_growth_rate

    # FA
    answer = time_in_years
    return answer