def solve():
    """Index: 3433.
    Returns: the maximum time the second runner can remain stopped.
    """
    # L1
    time_elapsed = 56 # After 56 minutes
    second_runner_pace = 7 # second runs at an average pace of 7 minutes per mile
    second_runner_distance = time_elapsed / second_runner_pace

    # L2
    first_runner_pace = 8 # first runs at an average pace of 8 minutes per mile
    first_runner_distance = time_elapsed / first_runner_pace

    # L3
    distance_apart = second_runner_distance - first_runner_distance

    # L4
    max_stop_time = first_runner_pace

    # FA
    answer = max_stop_time
    return answer