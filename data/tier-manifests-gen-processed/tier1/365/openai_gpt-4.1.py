def solve():
    """Index: 365.
    Returns: the total time the eight runners took to finish the race (sum of all individual finish times).
    """
    # L1
    num_first_group = 5 # first five runners
    time_first_group = 8 # finish the race in 8 hours
    total_time_first_group = num_first_group * time_first_group

    # L2
    total_runners = 8 # eight runners
    num_second_group = total_runners - num_first_group

    # L3
    extra_time_second_group = 2 # finish the race 2 hours later
    time_second_group = time_first_group + extra_time_second_group

    # L4
    total_time_second_group = time_second_group * num_second_group

    # L5
    answer = total_time_second_group + total_time_first_group
    return answer