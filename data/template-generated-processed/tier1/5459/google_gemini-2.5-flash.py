def solve():
    """Index: 5459.
    Returns: the total kilometers traveled by the driver during these 5 days.
    """
    # L1
    days_mon_wed = 3 # From Monday to Wednesday
    hours_per_day = 2 # 2 hours each day
    hours_mon_wed = days_mon_wed * hours_per_day

    # L2
    speed_mon_wed = 12 # average speed of 12 kilometers per hour
    distance_mon_wed = hours_mon_wed * speed_mon_wed

    # L3
    days_thu_fri = 2 # From Thursday to Friday
    hours_thu_fri = days_thu_fri * hours_per_day

    # L4
    speed_thu_fri = 9 # average speed of 9 kilometers per hour
    distance_thu_fri = hours_thu_fri * speed_thu_fri

    # L5
    total_distance = distance_mon_wed + distance_thu_fri

    # FA
    answer = total_distance
    return answer