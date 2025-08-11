def solve():
    """Index: 5005.
    Returns: the total hours Melissa spends driving in a year.
    """
    # L1
    trips_per_month = 2 # twice each month
    hours_per_trip = 3 # 3 hours to drive to town and back
    hours_per_month = trips_per_month * hours_per_trip

    # L2
    months_per_year = 12 # WK
    total_hours_per_year = hours_per_month * months_per_year

    # FA
    answer = total_hours_per_year
    return answer