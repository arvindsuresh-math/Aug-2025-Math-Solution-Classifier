def solve():
    """Index: 5616.
    Returns: the number of seconds Xena has before the dragon can burn her.
    """
    # L1
    head_start_distance = 600 # Xena has a 600 foot head start
    burn_distance = 120 # if it gets within 120 feet of her
    distance_to_close = head_start_distance - burn_distance

    # L2
    dragon_speed = 30 # the dragon flies 30 feet per second
    xena_speed = 15 # Xena runs 15 feet per second
    relative_speed = dragon_speed - xena_speed

    # L3
    time_to_burn = distance_to_close / relative_speed

    # FA
    answer = time_to_burn
    return answer