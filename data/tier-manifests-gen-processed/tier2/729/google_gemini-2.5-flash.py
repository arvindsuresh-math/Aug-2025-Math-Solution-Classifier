def solve():
    """Index: 729.
    Returns: the total distance John traveled.
    """
    # L1
    speed_with_dog = 6 # runs at 6 miles per hour when he is being dragged by his 100-pound German Shepherd dog
    duration_with_dog = 0.5 # for 30 minutes
    distance_with_dog = speed_with_dog * duration_with_dog

    # L2
    speed_alone = 4 # jogs at a speed of 4 miles per hour when he runs alone
    duration_alone = 0.5 # an additional 30 minutes by himself
    distance_alone = speed_alone * duration_alone

    # L3
    total_distance = distance_with_dog + distance_alone

    # FA
    answer = total_distance
    return answer