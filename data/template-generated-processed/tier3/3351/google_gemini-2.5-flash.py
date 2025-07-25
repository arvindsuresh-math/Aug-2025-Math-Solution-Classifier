def solve():
    """Index: 3351.
    Returns: the total cost Jefferson paid for the carriage.
    """
    # L1
    distance_miles = 20 # It is 20 miles away
    horse_speed_mph = 10 # The horse can go 10 miles per hour
    travel_hours = distance_miles / horse_speed_mph

    # L2
    cost_per_hour = 30 # It cost $30 per hour
    hourly_fee_cost = cost_per_hour * travel_hours

    # L3
    flat_fee = 20 # plus a flat fee of $20
    total_cost = hourly_fee_cost + flat_fee

    # FA
    answer = total_cost
    return answer