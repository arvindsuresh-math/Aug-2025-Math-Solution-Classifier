def solve():
    """Index: 582.
    Returns: the number of tomatoes Haruto has left after giving half to his friend.
    """
    # L1
    total_tomatoes = 127 # the plants grew 127 tomatoes
    tomatoes_eaten = 19 # Birds had eaten 19 of the tomatoes
    tomatoes_left = total_tomatoes - tomatoes_eaten

    # L2
    divisor = 2 # gave half of his tomatoes
    tomatoes_after_giving = tomatoes_left / divisor

    # FA
    answer = tomatoes_after_giving
    return answer