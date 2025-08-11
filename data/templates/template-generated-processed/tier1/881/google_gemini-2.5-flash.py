def solve():
    """Index: 881.
    Returns: the total amount Mark will spend on theater visits.
    """
    # L1
    performance_duration_hours = 3 # One performance lasts 3 hours
    price_per_hour = 5 # $5 for each hour
    price_per_performance = performance_duration_hours * price_per_hour

    # L2
    num_weeks = 6 # in 6 weeks
    total_spend = num_weeks * price_per_performance

    # FA
    answer = total_spend
    return answer