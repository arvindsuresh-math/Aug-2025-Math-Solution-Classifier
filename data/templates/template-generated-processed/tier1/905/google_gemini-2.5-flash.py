def solve():
    """Index: 905.
    Returns: the total number of cans of soda one machine can produce in 8 hours.
    """
    # L1
    minutes_per_hour = 60 # WK
    production_cycle_minutes = 30 # every 30 minutes
    sets_per_hour = minutes_per_hour / production_cycle_minutes
    total_hours = 8 # in 8 hours
    total_sets_of_30_minutes = total_hours * sets_per_hour

    # L2
    cans_per_cycle = 30 # produces 30 cans of soda
    total_cans = cans_per_cycle * total_sets_of_30_minutes

    # FA
    answer = total_cans
    return answer