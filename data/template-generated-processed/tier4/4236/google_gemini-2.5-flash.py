def solve():
    """Index: 4236.
    Returns: the total money spent in dollars.
    """
    # L1
    arcade_hours = 3 # 3 hours
    minutes_per_hour = 60 # WK
    total_minutes = arcade_hours * minutes_per_hour

    # L2
    minutes_per_use = 6 # every 6 minutes
    num_times_coins_in = total_minutes / minutes_per_use

    # L3
    cost_per_use = 0.5 # $.50 for every 6 minutes
    total_spent_dollars = num_times_coins_in * cost_per_use

    # FA
    answer = total_spent_dollars
    return answer