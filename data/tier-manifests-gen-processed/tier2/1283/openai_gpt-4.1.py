def solve():
    """Index: 1283.
    Returns: how much more Dan made doing the good work compared to the lower-paid work.
    """
    # L1
    low_paid_tasks = 400 # 400 work tasks
    low_paid_rate = 0.25 # $0.25 each
    low_paid_total = low_paid_tasks * low_paid_rate

    # L2
    high_paid_tasks = 5 # 5 work tasks
    high_paid_rate = 2.00 # $2.00 each
    high_paid_total = high_paid_tasks * high_paid_rate

    # L3
    difference = low_paid_total - high_paid_total

    # FA
    answer = difference
    return answer