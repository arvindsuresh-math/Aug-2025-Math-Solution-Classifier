def solve():
    """Index: 64.
    Returns: the total amount James earns per week.
    """
    # L1
    main_job_hourly_rate = 20 # James earns $20 an hour while working at his main job
    less_percent = 0.2 # 20% less
    less_earning_second_job = main_job_hourly_rate * less_percent

    # L2
    second_job_hourly_rate = main_job_hourly_rate - less_earning_second_job

    # L3
    main_job_hours = 30 # He works 30 hours at his main job
    main_job_earnings = main_job_hourly_rate * main_job_hours

    # L4
    second_job_hours_divisor = 2 # half that much at his second job
    second_job_hours = main_job_hours / second_job_hours_divisor

    # L5
    second_job_earnings = second_job_hours * second_job_hourly_rate

    # L6
    total_weekly_earnings = main_job_earnings + second_job_earnings

    # FA
    answer = total_weekly_earnings
    return answer