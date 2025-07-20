def solve():
    """Index: 5807.
    Returns: the total time, in minutes, the Polar Bears spent circling the island over that weekend.
    """
    # L2
    time_per_round = 30 # 30 minutes to fully navigate
    additional_rounds_saturday = 10 # 10 more round that day
    time_additional_rounds_saturday = additional_rounds_saturday * time_per_round

    # L3
    initial_rounds_saturday = 1 # rounding the island once
    time_initial_round_saturday = initial_rounds_saturday * time_per_round
    total_time_saturday = time_additional_rounds_saturday + time_initial_round_saturday

    # L4
    rounds_sunday = 15 # 15 rounds
    total_time_sunday = rounds_sunday * time_per_round

    # L5
    total_time_weekend = total_time_saturday + total_time_sunday

    # FA
    answer = total_time_weekend
    return answer