def solve():
    """Index: 7197.
    Returns: the total number of turtles taken into the conservation center.
    """
    # L1
    multiplier_twice = 2 # twice more
    green_turtles = 800 # number of green turtles is 800
    more_hawksbill_turtles = multiplier_twice * green_turtles

    # L2
    total_hawksbill_turtles = green_turtles + more_hawksbill_turtles

    # L3
    total_turtles_conservation_center = total_hawksbill_turtles + green_turtles

    # FA
    answer = total_turtles_conservation_center
    return answer