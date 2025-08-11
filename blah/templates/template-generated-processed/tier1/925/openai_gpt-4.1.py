def solve():
    """Index: 925.
    Returns: the total number of customers served by Ann, Becky, and Julia that day.
    """
    # L1
    ann_hours = 8 # every day for 8 hours
    becky_hours = 8 # every day for 8 hours
    num_full_shift_workers = 2 # Ann and Becky
    total_full_shift_hours = num_full_shift_workers * ann_hours

    # L2
    julia_hours = 6 # Julia was working only for 6 hours
    total_hours = total_full_shift_hours + julia_hours

    # L3
    customers_per_hour = 7 # Each of them is providing service to 7 customers per hour
    total_customers = customers_per_hour * total_hours

    # FA
    answer = total_customers
    return answer