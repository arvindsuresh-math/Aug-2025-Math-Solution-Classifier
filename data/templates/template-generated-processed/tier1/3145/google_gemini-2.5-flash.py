def solve():
    """Index: 3145.
    Returns: how much more it cost Aldrich to rent the ski boat than Ken to rent a sailboat over two days.
    """
    # L1
    sailboat_hourly_rate = 60 # $60 to rent a sailboat (interpreted as hourly by solution)
    hours_rented_per_day = 3 # three hours a day
    ken_cost_per_day = sailboat_hourly_rate * hours_rented_per_day

    # L2
    ski_boat_hourly_rate = 80 # $80 per hour to rent a ski boat
    aldrich_cost_per_day = ski_boat_hourly_rate * hours_rented_per_day

    # L3
    daily_cost_difference = aldrich_cost_per_day - ken_cost_per_day

    # L4
    num_days = 2 # in two days
    total_cost_difference = daily_cost_difference * num_days

    # FA
    answer = total_cost_difference
    return answer