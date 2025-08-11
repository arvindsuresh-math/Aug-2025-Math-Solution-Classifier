def solve():
    """Index: 1044.
    Returns: the total cost of transmitting the advertisements during the race.
    """
    # L1
    num_advertisements = 5 # five advertisements
    duration_per_ad = 3 # lasting 3 minutes each
    total_duration_minutes = num_advertisements * duration_per_ad

    # L2
    cost_per_minute = 4000 # One minute of advertising costs $4000
    total_cost = total_duration_minutes * cost_per_minute

    # FA
    answer = total_cost
    return answer