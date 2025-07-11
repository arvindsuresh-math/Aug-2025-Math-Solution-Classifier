def solve():
    """Index: 532.
    Returns: the total number of golf balls purchased.
    """
    # L1
    dan_dozens = 5 # Dan buys 5 dozen
    golf_balls_per_dozen = 12 # assuming 12 golf balls are 1 dozen
    dan_golf_balls = dan_dozens * golf_balls_per_dozen

    # L2
    gus_dozens = 2 # Gus buys 2 dozen
    gus_golf_balls = gus_dozens * golf_balls_per_dozen

    # L3
    chris_golf_balls = 48 # Chris buys 48 golf balls
    total_golf_balls = dan_golf_balls + gus_golf_balls + chris_golf_balls

    # FA
    answer = total_golf_balls
    return answer