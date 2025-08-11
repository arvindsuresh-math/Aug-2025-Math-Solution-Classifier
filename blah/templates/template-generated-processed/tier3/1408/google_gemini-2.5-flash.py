def solve():
    """Index: 1408.
    Returns: the total miles Nicki ran for the year.
    """
    # L1
    weeks_in_year = 52 # WK
    halves_in_year = 2 # WK
    weeks_per_half_year = weeks_in_year / halves_in_year

    # L2
    miles_first_half_per_week = 20 # 20 miles per week
    total_miles_first_half = miles_first_half_per_week * weeks_per_half_year

    # L3
    miles_second_half_per_week = 30 # 30 miles per week
    total_miles_second_half = miles_second_half_per_week * weeks_per_half_year

    # L4
    total_miles_year = total_miles_first_half + total_miles_second_half

    # FA
    answer = total_miles_year
    return answer