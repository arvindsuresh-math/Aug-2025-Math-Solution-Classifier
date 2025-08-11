def solve():
    """Index: 1044.
    Returns: the total cost of transmitting the advertisements during the race.
    """
    # L1
    num_ads = 5 # five advertisements
    minutes_per_ad = 3 # 3 minutes each
    total_minutes = num_ads * minutes_per_ad

    # L2
    cost_per_minute = 4000 # One minute of advertising costs $4000
    total_cost = total_minutes * cost_per_minute

    # FA
    answer = total_cost
    return answer