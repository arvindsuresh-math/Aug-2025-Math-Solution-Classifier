def solve():
    """Index: 845.
    Returns: the total number of different actors that can be on the show in one hour.
    """
    # L1
    minutes_per_hour = 60 # WK
    actor_time_per_set = 15 # 15 minutes
    num_sets_of_actors = minutes_per_hour / actor_time_per_set

    # L2
    actors_per_set = 5 # 5 actors at a time
    total_actors = num_sets_of_actors * actors_per_set

    # FA
    answer = total_actors
    return answer