def solve(
    hourly_rate_main_job: float = 20,  # James earns $20 an hour at his main job
    percent_less_second_job: float = 0.2,  # He earns 20% less at his second job
    hours_main_job: int = 30,  # He works 30 hours at his main job
    fraction_hours_second_job: float = 0.5  # He works half that much at his second job
):
    """Index: 64.
    Returns: James's total weekly earnings from both jobs.
    """

    #: L1
    hourly_rate_reduction = hourly_rate_main_job - percent_less_second_job # eval: 19.8 = 20 - 0.2

    #: L2
    hourly_rate_second_job = hourly_rate_main_job - hourly_rate_reduction # eval: 0.1999999999999993 = 20 - 19.8

    #: L3
    earnings_main_job = hourly_rate_main_job * hours_main_job # eval: 600 = 20 * 30

    #: L4
    hours_second_job = hours_main_job * fraction_hours_second_job # eval: 15.0 = 30 * 0.5

    #: L5
    earnings_second_job = hourly_rate_second_job * hours_second_job # eval: 2.9999999999999893 = 0.1999999999999993 * 15.0

    #: L6
    total_weekly_earnings = earnings_main_job + earnings_second_job # eval: 603.0 = 600 + 2.9999999999999893

    #: FA
    answer = total_weekly_earnings
    return answer # eval: return 603.0
