def solve():
    """Index: 125.
    Returns: Haley's height after a specified number of years.
    """
    # L1
    growth_rate_per_year = 3 # 3 inches every year
    num_years = 10 # after 10 years
    total_growth = growth_rate_per_year * num_years

    # L2
    current_height = 20 # currently 20 inches tall
    final_height = current_height + total_growth

    # FA
    answer = final_height
    return answer