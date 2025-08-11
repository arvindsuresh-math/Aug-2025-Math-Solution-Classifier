def solve():
    """Index: 7069.
    Returns: the total combined rainfall in inches for three days.
    """
    # L1
    monday_hours = 7 # 7 hours on Monday
    monday_rate = 1 # 1 inch per hour
    monday_rainfall = monday_hours * monday_rate

    # L2
    tuesday_hours = 4 # 4 hours on Tuesday
    tuesday_rate = 2 # 2 inches per hour
    tuesday_rainfall = tuesday_hours * tuesday_rate

    # L3
    twice_multiplier = 2 # twice that of the previous day
    wednesday_rate = twice_multiplier * tuesday_rate

    # L4
    wednesday_hours = 2 # 2 hours
    wednesday_rainfall = wednesday_hours * wednesday_rate

    # L5
    total_rainfall = monday_rainfall + tuesday_rainfall + wednesday_rainfall

    # FA
    answer = total_rainfall
    return answer