def solve():
    """Index: 173.
    Returns: the head start in seconds the turtle needs to finish in a tie.
    """
    # L1
    race_distance = 20 # 20 foot-race
    hare_speed = 10 # runs 10 feet/second
    hare_run_time = race_distance / hare_speed

    # L2
    turtle_speed = 1 # crawls 1 foot/second
    turtle_run_time = race_distance / turtle_speed

    # L3
    head_start_needed = turtle_run_time - hare_run_time

    # FA
    answer = head_start_needed
    return answer