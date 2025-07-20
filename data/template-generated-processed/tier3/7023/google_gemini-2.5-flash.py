def solve():
    """Index: 7023.
    Returns: the total number of hours Iggy spends running.
    """
    # L1
    monday_miles = 3 # On Monday, he runs 3 miles
    tuesday_miles = 4 # On Tuesday, he runs 4 miles
    wednesday_miles = 6 # On Wednesday, he runs 6 miles
    thursday_miles = 8 # On Thursday, he runs 8 miles
    friday_miles = 3 # On Friday, he runs 3 miles
    total_miles_run = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles

    # L2
    pace_minutes_per_mile = 10 # 1 mile in 10 minutes
    total_minutes_run = total_miles_run * pace_minutes_per_mile

    # L3
    minutes_per_hour = 60 # WK
    total_hours_run = total_minutes_run / minutes_per_hour

    # FA
    answer = total_hours_run
    return answer