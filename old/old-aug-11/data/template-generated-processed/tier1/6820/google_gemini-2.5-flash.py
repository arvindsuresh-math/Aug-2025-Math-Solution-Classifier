def solve():
    """Index: 6820.
    Returns: the total number of hours Jade and Krista drove altogether.
    """
    # L1
    trip_days = 3 # road trip for 3 days
    jade_hours_per_day = 8 # Jade had to drive 8 hours
    jade_total_hours = trip_days * jade_hours_per_day

    # L2
    krista_hours_per_day = 6 # Krista had to drive 6 hours
    krista_total_hours = trip_days * krista_hours_per_day

    # L3
    total_driving_hours = jade_total_hours + krista_total_hours

    # FA
    answer = total_driving_hours
    return answer