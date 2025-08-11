def solve():
    """Index: 125.
    Returns: Haley's height after 10 years.
    """
    # L1
    growth_rate_per_year = 3 # grows at the rate of 3 inches every year
    years = 10 # after 10 years
    total_growth = growth_rate_per_year * years

    # L2
    current_height = 20 # currently 20 inches tall
    height_after_years = current_height + total_growth

    # FA
    answer = height_after_years
    return answer