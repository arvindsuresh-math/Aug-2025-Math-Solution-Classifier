def solve():
    """Index: 1879.
    Returns: the average number of billboards seen per hour.
    """
    # L1
    billboards_hour_1 = 17 # 17 billboards
    billboards_hour_2 = 20 # 20 billboards
    billboards_hour_3 = 23 # 23 billboards
    total_billboards = billboards_hour_1 + billboards_hour_2 + billboards_hour_3

    # L2
    total_hours = 3 # over 3 hours
    average_billboards_per_hour = total_billboards / total_hours

    # FA
    answer = average_billboards_per_hour
    return answer