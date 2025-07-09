def solve(
    hourly_wage_main: float = 20,  # James earns $20 an hour at his main job
    percent_less_second_job: float = 0.2,  # He earns 20% less at his second job
    hours_main_job: int = 30  # He works 30 hours at his main job
):
    """Index: 64.
    Returns: the total amount James earns per week from both jobs.
    """

    #: L1
    wage_reduction = hourly_wage_main * percent_less_second_job # eval: 4.0 = 20 * 0.2

    #: L2

    #: L3
    earnings_main = hourly_wage_main * hours_main_job # eval: 600 = 20 * 30

    #: L4
    hours_second_job = hours_main_job / 2 # eval: 15.0 = 30 / 2

    #: L5
    earnings_second = hours_second_job * hourly_wage_main # eval: 300.0 = 15.0 * 20

    #: L6
    total_earnings = earnings_main + earnings_second # eval: 900.0 = 600 + 300.0

    #: FA
    answer = total_earnings
    return answer # eval: return 900.0
