def solve():
    """Index: 1004.
    Returns: the total cost for Kamil to hire the two professionals for the renovation.
    """
    # L1
    professionals = 2 # two professionals
    hours_per_day = 6 # work for him 6 hours a day
    total_hours_per_day = hours_per_day * professionals

    # L2
    days = 7 # for 7 days
    total_hours = days * total_hours_per_day

    # L3
    hourly_rate = 15 # paid $15 per hour of work
    total_cost = total_hours * hourly_rate

    # FA
    answer = total_cost
    return answer