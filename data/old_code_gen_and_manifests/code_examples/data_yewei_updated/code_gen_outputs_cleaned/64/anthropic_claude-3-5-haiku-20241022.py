def solve(
    hourly_rate_main_job: float = 20,  # James earns $20 an hour at his main job
    percent_less_second_job: float = 0.2,  # He earns 20% less at his second job
    hours_main_job: int = 30,  # He works 30 hours at his main job
    hours_second_job: int = 15  # Half the hours of his main job
):
    """Index: 64.
    Returns: James's total weekly earnings from both jobs.
    """
    #: L1
    hourly_rate_reduction = hourly_rate_main_job * percent_less_second_job

    #: L2
    hourly_rate_second_job = hourly_rate_main_job - hourly_rate_reduction

    #: L3
    earnings_main_job = hourly_rate_main_job * hours_main_job

    #: L4
    # hours_second_job is already calculated as half of hours_main_job

    #: L5
    earnings_second_job = hourly_rate_second_job * hours_second_job

    #: L6
    total_weekly_earnings = earnings_main_job + earnings_second_job

    answer = total_weekly_earnings  # FINAL ANSWER
    return answer