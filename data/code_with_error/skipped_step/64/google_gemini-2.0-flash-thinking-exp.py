def solve(
    main_job_hourly_rate: int = 20, # James earns $20 an hour
    second_job_pay_reduction_percent: int = 20, # He earns 20% less
    main_job_hours: int = 30 # He works 30 hours at his main job
):
    """Index: 64.
    Returns: the total amount James earns per week from both jobs.
    """

    #: L1

    #: L2
    second_job_hourly_rate = main_job_hourly_rate - main_job_hourly_rate

    #: L3
    main_job_earnings = main_job_hourly_rate * main_job_hours

    #: L4
    second_job_hours = main_job_hours / 2

    #: L5
    second_job_earnings = second_job_hours * second_job_hourly_rate

    #: L6
    total_weekly_earnings = main_job_earnings + second_job_earnings

    #: FA
    answer = total_weekly_earnings
    return answer