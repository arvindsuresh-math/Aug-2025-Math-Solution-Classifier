def solve():
    """Index: 1978.
    Returns: the total number of miles Alice will have walked that week by Friday.
    """
    # L1
    miles_to_school = 10 # walks 10 miles
    miles_from_school = 12 # walks 12 miles through a forest
    daily_miles_monday = miles_to_school + miles_from_school

    # L2
    remaining_days = 4 # other 4 days, from Tuesday to Friday
    miles_other_days = remaining_days * daily_miles_monday

    # L3
    total_miles_week = daily_miles_monday + miles_other_days

    # FA
    answer = total_miles_week
    return answer