def solve(
        main_job_hourly_rate: int = 20, # James earns $20 an hour while working at his main job
        second_job_pay_reduction_percent: float = 0.20, # He earns 20% less while working his second job
        main_job_hours: int = 30, # He works 30 hours at his main job
        second_job_hours_factor: float = 0.5 # half that much at his second job
    ):
    """Index: 64.
    Returns: the total amount James earns per week from both jobs.
    """

    #: L1
    second_job_reduction_amount = main_job_hourly_rate * second_job_pay_reduction_percent # eval: 4.0 = 20 * 0.2

    #: L2
    second_job_hourly_rate = main_job_hourly_rate - second_job_reduction_amount # eval: 16.0 = 20 - 4.0

    #: L3
    main_job_earnings = main_job_hourly_rate * main_job_hours # eval: 600 = 20 * 30

    #: L4
    second_job_hours = main_job_hours * second_job_hours_factor # eval: 15.0 = 30 * 0.5

    #: L5
    second_job_earnings = second_job_hours * second_job_hourly_rate # eval: 240.0 = 15.0 * 16.0

    #: L6
    total_weekly_earnings = main_job_earnings - second_job_earnings # eval: 360.0 = 600 - 240.0

    #: FA
    answer = total_weekly_earnings
    return answer # eval: return 360.0
