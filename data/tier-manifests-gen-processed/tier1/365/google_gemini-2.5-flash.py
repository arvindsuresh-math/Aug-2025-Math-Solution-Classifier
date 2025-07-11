def solve():
    """Index: 365.
    Returns: the total time the eight runners took to finish the race.
    """
    # L1
    num_first_group_runners = 5 # first five runners
    time_first_group = 8 # finish the race in 8 hours
    total_time_first_group = num_first_group_runners * time_first_group

    # L2
    total_runners = 8 # eight runners
    num_second_group_runners = total_runners - num_first_group_runners

    # L3
    time_later = 2 # 2 hours later
    time_second_group = time_first_group + time_later

    # L4
    total_time_second_group = time_second_group * num_second_group_runners

    # L5
    total_time_all_runners = total_time_second_group + total_time_first_group

    # FA
    answer = total_time_all_runners
    return answer