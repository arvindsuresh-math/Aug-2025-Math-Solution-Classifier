def solve():
    """Index: 1900.
    Returns: the total number of yards he threw the ball in the two days.
    """
    # L1
    times_thrown_saturday = 20 # threw the ball twenty times
    distance_50_deg = 20 # throws a football 20 yards when the temperature is 50 degrees Fahrenheit
    yards_saturday = times_thrown_saturday * distance_50_deg

    # L2
    multiplier_twice = 2 # ball moves twice as far
    distance_80_deg = multiplier_twice * distance_50_deg

    # L3
    times_thrown_sunday = 30 # threw the ball 30 times
    yards_sunday = times_thrown_sunday * distance_80_deg

    # L4
    total_yards = yards_sunday + yards_saturday

    # FA
    answer = total_yards
    return answer