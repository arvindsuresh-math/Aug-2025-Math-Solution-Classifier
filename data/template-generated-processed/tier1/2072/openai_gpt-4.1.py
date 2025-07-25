def solve():
    """Index: 2072.
    Returns: how many times faster than the first popsicle the last popsicle's remains melt.
    """
    # L1
    multiplier = 2 # melt twice as fast as the previous one
    first_speed = 1 # WK (the first popsicle's speed is the base)
    second_speed = multiplier * first_speed

    # L2
    third_speed = multiplier * second_speed

    # L3
    fourth_speed = multiplier * third_speed

    # L4
    fifth_speed = multiplier * fourth_speed

    # L5
    sixth_speed = multiplier * fifth_speed

    # FA
    answer = sixth_speed
    return answer