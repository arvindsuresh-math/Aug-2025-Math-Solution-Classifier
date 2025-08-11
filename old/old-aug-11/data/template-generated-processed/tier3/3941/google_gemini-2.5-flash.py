def solve():
    """Index: 3941.
    Returns: the additional speed Timmy needs to go.
    """
    # L1
    trial_speed_1 = 36 # goes 36
    trial_speed_2 = 34 # 34
    trial_speed_3 = 38 # and 38 mph
    total_trial_speed = trial_speed_1 + trial_speed_2 + trial_speed_3

    # L2
    number_of_trials = 3 # three trial runs
    average_speed = total_trial_speed / number_of_trials

    # L3
    required_speed = 40 # needs to go 40 mph
    speed_difference = required_speed - average_speed

    # FA
    answer = speed_difference
    return answer