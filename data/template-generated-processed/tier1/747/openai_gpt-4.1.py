def solve():
    """Index: 747.
    Returns: the combined height of the two rockets in feet.
    """
    # L1
    first_rocket_height = 500 # can travel 500 ft in the air
    multiplier_for_second = 2 # can travel twice as high
    second_rocket_height = first_rocket_height * multiplier_for_second

    # L2
    total_height = first_rocket_height + second_rocket_height

    # FA
    answer = total_height
    return answer