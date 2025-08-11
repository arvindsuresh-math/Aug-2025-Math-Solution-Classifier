def solve():
    """Index: 1340.
    Returns: the total number of hours William rode his horse during the 6 days.
    """
    # L1
    max_hours_per_day = 6 # can ride his horse for 6 hours a day
    days_max_time = 2 # only used the maximum riding time twice
    hours_max_days = max_hours_per_day * days_max_time

    # L2
    short_ride_hours = 1.5 # rode his horse for only 1.5 hours a day
    days_short_ride = 2 # on two days
    hours_short_days = short_ride_hours * days_short_ride

    # L3
    half_time_factor = 0.5 # half the maximum time
    hours_half_day = max_hours_per_day * half_time_factor

    # L4
    days_half_time = 2 # for the next two days
    hours_half_days = days_half_time * hours_half_day

    # L5
    total_hours = hours_max_days + hours_short_days + hours_half_days

    # FA
    answer = total_hours
    return answer