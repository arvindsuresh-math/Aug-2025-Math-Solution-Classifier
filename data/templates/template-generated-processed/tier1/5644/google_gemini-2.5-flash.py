def solve():
    """Index: 5644.
    Returns: the total number of permits Andrew stamps today.
    """
    # L1
    num_appointments = 2 # 2 3-hour appointments
    hours_per_appointment = 3 # 3-hour appointments
    total_appointment_hours = num_appointments * hours_per_appointment

    # L2
    total_workday_hours = 8 # 8-hour workday
    stamping_hours = total_workday_hours - total_appointment_hours

    # L3
    permits_per_hour = 50 # stamp 50 permit applications an hour
    total_permits_stamped = permits_per_hour * stamping_hours

    # FA
    answer = total_permits_stamped
    return answer