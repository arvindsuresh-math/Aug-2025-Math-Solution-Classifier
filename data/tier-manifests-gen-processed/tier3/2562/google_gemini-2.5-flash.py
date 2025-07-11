from fractions import Fraction

def solve():
    """Index: 2562.
    Returns: the time it takes for Jason to eat all potatoes in hours.
    """
    # L1
    time_per_three_potatoes_minutes = 20 # three potatoes in 20 minutes
    minutes_per_hour = 60 # 1 hour is 60 minutes
    time_per_three_potatoes_hours = Fraction(time_per_three_potatoes_minutes, minutes_per_hour)

    # L2
    potatoes_per_interval = 3 # three potatoes
    potatoes_per_hour = potatoes_per_interval / time_per_three_potatoes_hours

    # L3
    total_potatoes = 27 # all 27 potatoes
    total_time_hours = total_potatoes / potatoes_per_hour

    # FA
    answer = total_time_hours
    return answer