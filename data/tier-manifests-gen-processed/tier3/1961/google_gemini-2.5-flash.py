def solve():
    """Index: 1961.
    Returns: the number of days to complete the order.
    """
    # L1
    total_candies_needed = 4000 # produce 4000 candies
    production_rate_per_hour = 50 # produces 50 candies per hour
    total_hours_needed = total_candies_needed / production_rate_per_hour

    # L2
    hours_per_day = 10 # works for 10 hours every day
    total_days_needed = total_hours_needed / hours_per_day

    # FA
    answer = total_days_needed
    return answer