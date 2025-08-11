def solve():
    """Index: 3181.
    Returns: the time it takes for the dog to catch the sheep.
    """
    # L1
    dog_speed = 20 # sheepdog can run 20 feet per second
    sheep_speed = 12 # sheep can run 12 feet per second
    speed_difference = dog_speed - sheep_speed

    # L2
    initial_distance = 160 # A sheep standing 160 feet away
    time_to_catch = initial_distance / speed_difference

    # FA
    answer = time_to_catch
    return answer