def solve():
    """Index: 1004.
    Returns: the total cost to hire the professionals.
    """
    # L1
    hours_per_day_per_professional = 6 # 6 hours a day
    num_professionals = 2 # two professionals
    total_hours_per_day = hours_per_day_per_professional * num_professionals

    # L2
    num_days_worked = 7 # for 7 days
    total_hours_worked = num_days_worked * total_hours_per_day

    # L3
    hourly_rate = 15 # $15 per hour of work
    total_cost = total_hours_worked * hourly_rate

    # FA
    answer = total_cost
    return answer