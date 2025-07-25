def solve():
    """Index: 881.
    Returns: the total amount Mark will spend on theater visits in 6 weeks.
    """
    # L1
    hours_per_performance = 3 # One performance lasts 3 hours
    price_per_hour = 5 # $5 for each hour
    price_per_performance = hours_per_performance * price_per_hour

    # L2
    num_weeks = 6 # in 6 weeks
    total_spent = num_weeks * price_per_performance

    # FA
    answer = total_spent
    return answer