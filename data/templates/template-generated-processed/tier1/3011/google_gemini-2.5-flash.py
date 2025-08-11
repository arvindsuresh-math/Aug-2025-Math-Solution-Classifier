def solve():
    """Index: 3011.
    Returns: the total hours Thomas will spend on training.
    """
    # L1
    days_in_month = 30 # for a month (30 days)
    additional_days = 12 # for the next 12 days
    total_days = days_in_month + additional_days

    # L2
    hours_per_day = 5 # trained for 5 hours every day
    total_training_hours = total_days * hours_per_day

    # FA
    answer = total_training_hours
    return answer