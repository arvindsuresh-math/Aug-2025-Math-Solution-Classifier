def solve():
    """Index: 2729.
    Returns: the total amount of money the three men will earn.
    """
    # L1
    pay_per_man_per_hour = 10 # $10 per hour
    men_count = 3 # 3 men
    earnings_per_job = pay_per_man_per_hour * men_count

    # L2
    num_jobs = 5 # 5 such similar jobs
    total_earnings = earnings_per_job * num_jobs

    # FA
    answer = total_earnings
    return answer