def solve():
    """Index: 5968.
    Returns: the tree's total height after 4 months.
    """
    # L1
    weeks_per_month = 4 # assuming each month is 4 weeks long
    num_months = 4 # after 4 months
    total_weeks_growing = num_months * weeks_per_month

    # L2
    growth_rate_per_week = 2 # grows at the rate of 2 feet per week
    height_increase = growth_rate_per_week * total_weeks_growing

    # L3
    current_height = 10 # currently 10 feet tall
    final_height = current_height + height_increase

    # FA
    answer = final_height
    return answer