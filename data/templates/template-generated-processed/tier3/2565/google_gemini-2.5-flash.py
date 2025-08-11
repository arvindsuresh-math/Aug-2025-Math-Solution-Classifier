def solve():
    """Index: 2565.
    Returns: the total number of steps John climbs.
    """
    # L1
    num_flights = 9 # 9 flights of stairs
    feet_per_flight = 10 # Each flight is 10 feet
    total_feet_climbed = num_flights * feet_per_flight

    # L2
    inches_per_foot = 12 # WK
    total_inches_climbed = total_feet_climbed * inches_per_foot

    # L3
    inches_per_step = 18 # each step is 18 inches
    total_steps = total_inches_climbed / inches_per_step

    # FA
    answer = total_steps
    return answer