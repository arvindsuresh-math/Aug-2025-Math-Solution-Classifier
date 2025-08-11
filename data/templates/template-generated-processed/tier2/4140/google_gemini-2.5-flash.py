def solve():
    """Index: 4140.
    Returns: the total points Michael scored during both years.
    """
    # L1
    junior_year_points = 260 # scored 260 points during his junior year
    senior_year_increase_factor = 1.20 # 20% more points during his senior year (100% + 20% = 120% or 1.20 times)
    senior_year_points = junior_year_points * senior_year_increase_factor

    # L2
    total_points = junior_year_points + senior_year_points

    # FA
    answer = total_points
    return answer