def solve():
    """Index: 6640.
    Returns: the total amount Noah would be billed for calls in a year.
    """
    # L1
    weeks_per_year = 52 # WK
    minutes_per_call = 30 # each call lasts 30 minutes
    total_call_minutes = weeks_per_year * minutes_per_call

    # L2
    cost_per_minute = 0.05 # $0.05 per call minute
    total_cost = total_call_minutes * cost_per_minute

    # FA
    answer = total_cost
    return answer