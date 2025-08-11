def solve():
    """Index: 4679.
    Returns: the number of baby sea turtles still on the sand.
    """
    # L1
    total_turtles = 42 # A total of 42 baby sea turtles
    fraction_denominator = 3 # One-third of them
    turtles_in_ocean = total_turtles / fraction_denominator

    # L2
    turtles_on_sand = total_turtles - turtles_in_ocean

    # FA
    answer = turtles_on_sand
    return answer