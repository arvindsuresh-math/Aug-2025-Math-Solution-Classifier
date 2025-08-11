def solve():
    """Index: 3479.
    Returns: the profit Pat can expect to make.
    """
    # L1
    hunting_hours = 5 # shark hunts for 5 hours
    fuel_cost_per_hour = 50 # boat fuel costs $50 an hour
    total_fuel_cost = hunting_hours * fuel_cost_per_hour

    # L2
    minutes_per_hour = 60 # WK
    total_hunting_minutes = hunting_hours * minutes_per_hour

    # L3
    time_per_shark = 10 # sees a shark about every 10 minutes
    num_sharks_seen = total_hunting_minutes / time_per_shark

    # L4
    earnings_per_photo = 15 # For every photo he takes he earns $15
    total_earnings_from_photos = num_sharks_seen * earnings_per_photo

    # L5
    profit = total_earnings_from_photos - total_fuel_cost

    # FA
    answer = profit
    return answer