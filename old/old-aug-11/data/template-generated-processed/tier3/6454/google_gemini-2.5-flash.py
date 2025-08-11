def solve():
    """Index: 6454.
    Returns: the number of turtles remaining on the log.
    """
    # L1
    original_turtles = 9 # nine turtles
    multiplier = 3 # three times the original number
    subtractor = 2 # Two less
    new_turtles_climbed = (original_turtles * multiplier) - subtractor

    # L2
    total_turtles_on_log = new_turtles_climbed + original_turtles

    # L3
    divisor = 2 # half of the large group
    remaining_turtles = total_turtles_on_log / divisor

    # FA
    answer = remaining_turtles
    return answer