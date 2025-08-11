def solve():
    """Index: 2535.
    Returns: the total money Jamie will have earned.
    """
    # L1
    days_per_week_delivery = 2 # delivers flyers 2 days each week
    hours_per_delivery_time = 3 # takes her 3 hours each time she delivers flyers
    hours_per_week = days_per_week_delivery * hours_per_delivery_time

    # L2
    weeks_delivered = 6 # After delivering flyers for 6 weeks
    total_hours_delivered = hours_per_week * weeks_delivered

    # L3
    hourly_rate = 10 # earns $10 an hour
    total_earnings = total_hours_delivered * hourly_rate

    # FA
    answer = total_earnings
    return answer