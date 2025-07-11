def solve():
    """Index: 905.
    Returns: the number of cans of soda one machine can produce in 8 hours.
    """
    # L1
    minutes_per_hour = 60 # WK
    set_minutes = 30 # every 30 minutes
    sets_per_hour = minutes_per_hour // set_minutes
    hours = 8 # in 8 hours
    total_sets = hours * sets_per_hour

    # L2
    cans_per_set = 30 # produces 30 cans of soda
    total_cans = cans_per_set * total_sets

    # FA
    answer = total_cans
    return answer