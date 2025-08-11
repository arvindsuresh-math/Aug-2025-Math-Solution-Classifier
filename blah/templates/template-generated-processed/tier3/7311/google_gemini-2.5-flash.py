def solve():
    """Index: 7311.
    Returns: the number of miles farther the superhero can run than the supervillain can drive in an hour.
    """
    # L1
    minutes_per_hour = 60 # WK
    superhero_time_per_interval = 4 # 4 minutes
    intervals_in_hour = minutes_per_hour / superhero_time_per_interval

    # L2
    miles_per_interval = 10 # 10 miles
    superhero_miles_per_hour = intervals_in_hour * miles_per_interval

    # L3
    supervillain_miles_per_hour = 100 # 100 miles per hour
    miles_farther = superhero_miles_per_hour - supervillain_miles_per_hour

    # FA
    answer = miles_farther
    return answer