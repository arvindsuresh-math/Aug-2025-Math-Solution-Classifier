def solve():
    """Index: 3431.
    Returns: the average earnings per minute.
    """
    # L1
    num_laps = 24 # 24 laps around the school
    meters_per_lap = 100 # One lap around the school is 100 meters
    total_meters_ran = num_laps * meters_per_lap

    # L2
    total_minutes = 12 # in 12 minutes
    meters_per_minute = total_meters_ran / total_minutes

    # L3
    dollars_per_hundred_meters = 3.5 # $3.5 for every one hundred meters
    hundred_meters_unit = 100 # every one hundred meters
    earnings_per_minute = dollars_per_hundred_meters / hundred_meters_unit * meters_per_minute

    # FA
    answer = earnings_per_minute
    return answer