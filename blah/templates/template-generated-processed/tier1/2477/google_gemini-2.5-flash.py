def solve():
    """Index: 2477.
    Returns: the money Mike received from his first job.
    """
    # L1
    second_job_pay_per_hour = 9 # $9 per hour
    second_job_hours_per_week = 12 # 12 hours a week
    second_job_earnings = second_job_pay_per_hour * second_job_hours_per_week

    # L2
    total_wages = 160 # total of $160 in wages
    first_job_earnings = total_wages - second_job_earnings

    # FA
    answer = first_job_earnings
    return answer