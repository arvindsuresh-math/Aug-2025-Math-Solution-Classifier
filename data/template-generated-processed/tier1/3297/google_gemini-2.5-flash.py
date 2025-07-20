def solve():
    """Index: 3297.
    Returns: the total miles Tom drives for the year.
    """
    # L1
    first_period_days = 183 # 183 days
    miles_per_day_first_period = 30 # 30 miles per day
    miles_first_period = first_period_days * miles_per_day_first_period

    # L2
    days_in_year = 365 # WK
    remaining_days = days_in_year - first_period_days

    # L3
    miles_per_day_rest_of_year = 35 # 35 miles per day
    miles_rest_of_year = miles_per_day_rest_of_year * remaining_days

    # L4
    total_miles = miles_first_period + miles_rest_of_year

    # FA
    answer = total_miles
    return answer