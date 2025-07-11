def solve():
    """Index: 532.
    Returns: the total number of golf balls purchased by Dan, Gus, and Chris.
    """
    # L1
    dan_dozen = 5 # Dan buys 5 dozen
    dozen = 12 # 12 golf balls are 1 dozen
    dan_balls = dan_dozen * dozen

    # L2
    gus_dozen = 2 # Gus buys 2 dozen
    gus_balls = gus_dozen * dozen

    # L3
    chris_balls = 48 # Chris buys 48 golf balls
    total_balls = dan_balls + gus_balls + chris_balls

    # FA
    answer = total_balls
    return answer