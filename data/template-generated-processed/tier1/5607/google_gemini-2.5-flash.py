def solve():
    """Index: 5607.
    Returns: the total amount Johnny makes over 5 days.
    """
    # L1
    hours_job1 = 3 # 3 hours working on a job
    pay_rate_job1 = 7 # paid $7 per hour
    earnings_job1 = hours_job1 * pay_rate_job1

    # L2
    hours_job2 = 2 # 2 hours working on a job
    pay_rate_job2 = 10 # paid $10 an hour
    earnings_job2 = hours_job2 * pay_rate_job2

    # L3
    hours_job3 = 4 # 4 hours working on a job
    pay_rate_job3 = 12 # paid $12 an hour
    earnings_job3 = hours_job3 * pay_rate_job3

    # L4
    total_daily_earnings = earnings_job1 + earnings_job2 + earnings_job3

    # L5
    num_days = 5 # 5 days in a row
    total_earnings_5_days = num_days * total_daily_earnings

    # FA
    answer = total_earnings_5_days
    return answer