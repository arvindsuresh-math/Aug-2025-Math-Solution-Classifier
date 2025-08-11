def solve():
    """Index: 5381.
    Returns: the average distance run by Johnny and Mickey.
    """
    # L1
    johnny_runs_times = 4 # Johnny runs around the block 4 times
    half_divisor = 2 # half of 4
    mickey_runs_times = johnny_runs_times / half_divisor

    # L2
    meters_per_block = 200 # One time around the block equals 200 meters
    mickey_distance = mickey_runs_times * meters_per_block

    # L3
    johnny_distance = johnny_runs_times * meters_per_block

    # L4
    total_distance = mickey_distance + johnny_distance

    # L5
    number_of_people = 2 # WK
    average_distance = total_distance / number_of_people

    # FA
    answer = average_distance
    return answer