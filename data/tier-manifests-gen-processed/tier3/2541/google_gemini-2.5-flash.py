def solve():
    """Index: 2541.
    Returns: the time it takes the peregrine falcon to dive the same distance.
    """
    # L1
    bald_eagle_speed = 100 # The bald eagle can dive at a speed of 100 miles per hour
    multiplier = 2 # twice that of the bald eagle
    peregrine_falcon_speed = bald_eagle_speed * multiplier

    # L3
    bald_eagle_time = 30 # it takes the bald eagle 30 seconds
    peregrine_falcon_time = bald_eagle_time * (bald_eagle_speed / peregrine_falcon_speed)

    # FA
    answer = peregrine_falcon_time
    return answer