def solve():
    """Index: 3900.
    Returns: the total wages for the new set of workers and days.
    """
    # L1
    num_workers_initial = 15 # 15 workers
    num_days_initial = 6 # 6 days
    equivalent_days_initial = num_workers_initial * num_days_initial

    # L2
    total_wages_initial = 9450 # $9450
    pay_per_worker_per_day = total_wages_initial / equivalent_days_initial

    # L3
    num_workers_new = 19 # 19 workers
    num_days_new = 5 # 5 days
    equivalent_days_new = num_workers_new * num_days_new

    # L4
    total_wages_new = pay_per_worker_per_day * equivalent_days_new

    # FA
    answer = total_wages_new
    return answer