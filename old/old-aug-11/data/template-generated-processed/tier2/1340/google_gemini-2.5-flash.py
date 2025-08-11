def solve():
    """Index: 1340.
    Returns: the total hours William rode his horse.
    """
    # L1
    max_riding_time_per_day = 6 # ride his horse for 6 hours a day
    days_at_max_time = 2 # used the maximum riding time twice
    hours_at_max_time = max_riding_time_per_day * days_at_max_time

    # L2
    riding_time_specific_day = 1.5 # rode his horse for only 1.5 hours a day
    num_specific_days = 2 # On two days
    hours_specific_days = riding_time_specific_day * num_specific_days

    # L3
    half_max_factor = 0.5 # half the maximum time
    hours_per_half_max_day = max_riding_time_per_day * half_max_factor

    # L4
    num_half_max_days = 2 # for the next two days
    total_hours_half_max_days = num_half_max_days * hours_per_half_max_day

    # L5
    total_riding_hours = hours_at_max_time + hours_specific_days + total_hours_half_max_days

    # FA
    answer = total_riding_hours
    return answer