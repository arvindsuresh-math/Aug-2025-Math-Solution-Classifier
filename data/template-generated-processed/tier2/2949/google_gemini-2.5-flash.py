def solve():
    """Index: 2949.
    Returns: the time Mrs. Parker has to use the bathroom.
    """
    # L2
    total_available_hours = 2.5 # time between 2:30 pm and 5 pm
    minutes_per_hour = 60 # WK
    total_available_minutes = total_available_hours * minutes_per_hour

    # L3
    oldest_daughter_time = 45 # used the bathroom for 45 minutes
    youngest_daughter_time = 30 # used the bathroom for another 30 minutes
    husband_time = 20 # used it for 20 minutes
    family_total_time = oldest_daughter_time + youngest_daughter_time + husband_time

    # L4
    mrs_parker_time = total_available_minutes - family_total_time

    # FA
    answer = mrs_parker_time
    return answer