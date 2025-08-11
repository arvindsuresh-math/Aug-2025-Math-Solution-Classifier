def solve():
    """Index: 582.
    Returns: the number of tomatoes Haruto has left.
    """
    # L1
    initial_tomatoes = 127 # plants grew 127 tomatoes
    eaten_by_birds = 19 # Birds had eaten 19 of the tomatoes
    tomatoes_after_birds = initial_tomatoes - eaten_by_birds

    # L2
    given_away_divisor = 2 # gave half of his tomatoes
    tomatoes_left = tomatoes_after_birds / given_away_divisor

    # FA
    answer = tomatoes_left
    return answer