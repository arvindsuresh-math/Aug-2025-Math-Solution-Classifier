def solve(
        main_job_hourly_rate: int = 20,  # James earns $20 an hour while working at his main job
        second_job_pay_reduction_percentage: float = 0.20,  # He earns 20% less while working his second job
        main_job_hours: int = 30,  # He works 30 hours at his main job
        second_job_hours_factor: float = 0.5  # half that much at his second job
    ):
    """Index: 64.
    Returns: the total amount James earns per week from both jobs.
    """
    #: L1
    less_earned_second_job = main_job_hourly_rate * second_job_pay_reduction_percentage

    #: L2
    second_job_hourly_rate = main_job_hourly_rate - less_earned_second_job

    #: L3
    earnings_main_job = main_job_hourly_rate * main_job_hours

    #: L4
    second_job_hours = main_job_hours * second_job_hours_factor

    #: L5
    earnings_second_job = second_job_hours * second_job_hourly_rate

    #: L6
    total_weekly_earnings = earnings_main_job + earnings_second_job

    answer = total_weekly_earnings # FINAL ANSWER
    return answer