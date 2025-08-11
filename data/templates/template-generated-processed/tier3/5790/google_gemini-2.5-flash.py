def solve():
    """Index: 5790.
    Returns: the number of hours Lisa needs to work to equal Greta's earnings.
    """
    # L1
    greta_hours_worked = 40 # Greta worked 40 hours
    greta_hourly_rate = 12 # paid $12 per hour
    greta_total_earnings = greta_hours_worked * greta_hourly_rate

    # L2
    lisa_hourly_rate = 15 # Lisa earned $15 per hour
    lisa_hours_needed = greta_total_earnings / lisa_hourly_rate

    # FA
    answer = lisa_hours_needed
    return answer