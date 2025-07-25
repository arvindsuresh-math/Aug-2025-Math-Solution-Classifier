def solve():
    """Index: 925.
    Returns: the total number of customers served by all three women that day.
    """
    # L1
    num_people_full_day = 2 # Ann, Becky
    hours_full_day = 8 # every day for 8 hours
    hours_ann_becky = num_people_full_day * hours_full_day

    # L2
    julia_hours = 6 # Julia had to finish her work earlier, so she was working only for 6 hours
    total_hours_worked = hours_ann_becky + julia_hours

    # L3
    customers_per_hour = 7 # providing service to 7 customers per hour
    total_customers_served = customers_per_hour * total_hours_worked

    # FA
    answer = total_customers_served
    return answer