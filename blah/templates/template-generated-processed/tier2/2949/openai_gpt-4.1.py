def solve():
    """Index: 2949.
    Returns: the number of minutes Mrs. Parker will have to use the bathroom to leave on time.
    """
    # L2
    total_hours = 2.5 # Between 2:30 pm and 5:00 pm, there are 2.5 hours.
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L3
    oldest_daughter_time = 45 # her oldest daughter used the bathroom for 45 minutes
    youngest_daughter_time = 30 # her youngest daughter used the bathroom for another 30 minutes
    husband_time = 20 # her husband used it for 20 minutes
    family_bathroom_time = oldest_daughter_time + youngest_daughter_time + husband_time

    # L4
    mrs_parker_time = total_minutes - family_bathroom_time

    # FA
    answer = mrs_parker_time
    return answer