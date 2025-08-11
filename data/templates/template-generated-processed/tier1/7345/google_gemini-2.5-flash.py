def solve():
    """Index: 7345.
    Returns: the total number of birds the cat caught.
    """
    # L1
    birds_day = 8 # 8 birds during the day
    multiplier_night = 2 # twice this many at night
    birds_night = birds_day * multiplier_night

    # L2
    total_birds = birds_day + birds_night

    # FA
    answer = total_birds
    return answer