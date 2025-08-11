def solve():
    """Index: 2729.
    Returns: the total amount of money the three men will earn after completing 5 jobs.
    """
    # L1
    pay_per_hour = 10 # pays each of them $10 per hour
    num_men = 3 # 3 men
    total_per_hour = pay_per_hour * num_men

    # L2
    num_jobs = 5 # 5 such similar jobs
    total_earnings = total_per_hour * num_jobs

    # FA
    answer = total_earnings
    return answer