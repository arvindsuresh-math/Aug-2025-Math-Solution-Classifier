def solve():
    """Index: 5918.
    Returns: the highest elevation reached by the balloon during the ride.
    """
    # L1
    rise_rate_pulled = 50 # rise at a rate of 50 feet per minute
    first_pull_duration = 15 # pulled the chain for 15 minutes
    elevation_after_first_pull = rise_rate_pulled * first_pull_duration

    # L2
    descend_rate_released = 10 # descend at a rate of 10 feet per minute
    first_release_duration = 10 # released the rope for 10 minutes
    descent_amount = descend_rate_released * first_release_duration

    # L3
    second_pull_duration = 15 # pulled the chain for another 15 minutes
    elevation_after_second_pull = rise_rate_pulled * second_pull_duration

    # L4
    highest_elevation = elevation_after_first_pull - descent_amount + elevation_after_second_pull

    # FA
    answer = highest_elevation
    return answer