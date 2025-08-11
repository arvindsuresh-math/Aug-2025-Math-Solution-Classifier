def solve():
    """Index: 2136.
    Returns: the number of school days it will take Jessica to meet the driving requirement.
    """
    # L1
    minutes_to_school = 20 # It takes 20 minutes to drive to school
    trips_per_day = 2 # to and from school
    minutes_per_day = minutes_to_school * trips_per_day

    # L2
    required_hours = 50 # 50 hours of driving
    minutes_per_hour = 60 # 60 minutes in 1 hour
    hours_in_hour = 1 # 1 hour
    required_minutes = required_hours * minutes_per_hour

    # L3
    school_days_needed = required_minutes / minutes_per_day

    # FA
    answer = school_days_needed
    return answer