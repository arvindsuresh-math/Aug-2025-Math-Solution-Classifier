def solve():
    """Index: 2477.
    Returns: the amount of money Mike received from his first job in dollars.
    """
    # L1
    second_job_rate = 9 # $9 per hour
    second_job_hours = 12 # 12 hours a week
    second_job_earnings = second_job_rate * second_job_hours

    # L2
    total_earnings = 160 # earned a total of $160 in wages this week
    first_job_earnings = total_earnings - second_job_earnings

    # FA
    answer = first_job_earnings
    return answer