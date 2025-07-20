def solve():
    """Index: 5808.
    Returns: the duration Fiona was cleaning in minutes.
    """
    # L1
    total_cleaning_hours = 8 # it takes 8 hours to clean the room
    lilly_time_denominator = 4 # A quarter of the time spent cleaning
    lilly_cleaning_hours = total_cleaning_hours / lilly_time_denominator

    # L2
    fiona_cleaning_hours = total_cleaning_hours - lilly_cleaning_hours

    # L3
    minutes_per_hour = 60 # WK
    fiona_cleaning_minutes = fiona_cleaning_hours * minutes_per_hour

    # FA
    answer = fiona_cleaning_minutes
    return answer