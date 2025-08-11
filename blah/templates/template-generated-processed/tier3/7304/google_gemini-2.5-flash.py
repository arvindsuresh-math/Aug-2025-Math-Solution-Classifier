def solve():
    """Index: 7304.
    Returns: the total number of days for all pollywogs to disappear from the pond.
    """
    # L1
    natural_disappearance_rate = 50 # constant rate of 50 pollywogs per day
    melvin_catch_rate = 10 # caught 10 pollywogs per day
    combined_rate_first_period = natural_disappearance_rate + melvin_catch_rate

    # L2
    first_period_days = 20 # For the first 20 days
    pollywogs_removed_first_period = combined_rate_first_period * first_period_days

    # L3
    initial_pollywogs = 2400 # initially contained 2400 pollywogs
    pollywogs_left_after_first_period = initial_pollywogs - pollywogs_removed_first_period

    # L4
    additional_days = pollywogs_left_after_first_period / natural_disappearance_rate

    # L5
    total_days = first_period_days + additional_days

    # FA
    answer = total_days
    return answer