def solve():
    """Index: 1596.
    Returns: the total number of kilometers Nina would travel during 2 years.
    """
    # L1
    regular_monthly_distance = 400 # travel at least 400 kilometers in one month
    double_distance_factor = 2 # twice that distance
    double_monthly_distance = regular_monthly_distance * double_distance_factor

    # L2
    years = 2 # 2 years
    months_per_year = 12 # WK
    total_months = years * months_per_year
    half_fraction = 0.5 # WK
    months_each_type = total_months * half_fraction

    # L3
    distance_regular_months = regular_monthly_distance * months_each_type

    # L4
    distance_double_months = double_monthly_distance * months_each_type

    # L5
    total_distance = distance_regular_months + distance_double_months

    # FA
    answer = total_distance
    return answer