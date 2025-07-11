def solve(
    hourly_wage_main_job: int = 20, # James earns $20 an hour while working at his main job.
    second_job_wage_reduction_rate: float = 0.2, # He earns 20% less while working his second job.
    hours_main_job: int = 30, # He works 30 hours at his main job
    hours_second_job_factor: float = 0.5 # and half that much at his second job.
):
    """Index: 64.
    Returns: the total amount James earns per week.
    """

    #: L1
    wage_reduction_amount = hourly_wage_main_job * second_job_wage_reduction_rate # eval: 4.0 = 20 * 0.2

    #: L2
    hourly_wage_second_job = hourly_wage_main_job + wage_reduction_amount # eval: 24.0 = 20 + 4.0

    #: L3
    earnings_main_job = hourly_wage_main_job * hours_main_job # eval: 600 = 20 * 30

    #: L4
    hours_second_job = hours_main_job * hours_second_job_factor # eval: 15.0 = 30 * 0.5

    #: L5
    earnings_second_job = hours_second_job * hourly_wage_second_job # eval: 360.0 = 15.0 * 24.0

    #: L6
    total_weekly_earnings = earnings_main_job + earnings_second_job # eval: 960.0 = 600 + 360.0

    #: FA
    answer = total_weekly_earnings
    return answer # eval: return 960.0
