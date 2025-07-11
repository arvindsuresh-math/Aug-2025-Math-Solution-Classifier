def solve():
    """Index: 64.
    Returns: the total amount James earns per week.
    """
    # L1
    main_job_hourly = 20 # James earns $20 an hour while working at his main job
    second_job_percent_less = 0.2 # He earns 20% less while working his second job
    second_job_hourly_less = main_job_hourly * second_job_percent_less

    # L2
    second_job_hourly = main_job_hourly - second_job_hourly_less

    # L3
    main_job_hours = 30 # He works 30 hours at his main job
    main_job_earnings = main_job_hourly * main_job_hours

    # L4
    second_job_hours = main_job_hours / 2

    # L5
    second_job_earnings = second_job_hours * second_job_hourly

    # L6
    total_earnings = main_job_earnings + second_job_earnings

    # FA
    answer = total_earnings
    return answer