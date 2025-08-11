def solve():
    """Index: 4732.
    Returns: the number of yards Kenneth will be past the finish line.
    """
    # L1
    race_distance = 500 # a 500-yard rowboat race
    biff_speed = 50 # Biff rows at a speed of 50 yards per minute
    time_biff_finishes = race_distance / biff_speed

    # L2
    kenneth_speed = 51 # Kenneth rows at a speed of 51 yards per minute
    distance_kenneth_travels = time_biff_finishes * kenneth_speed

    # L3
    yards_past_finish_line = distance_kenneth_travels - race_distance

    # FA
    answer = yards_past_finish_line
    return answer