def solve(
    sally_daily_wage: int = 6, # Sally makes $6 per day
    bob_daily_wage: int = 4, # Bob makes $4 per day
    fraction_saved: float = 0.5, # They both decide to work as babysitters and save half of what they've earned
    days_in_year: int = 365 # after a year
):
    """Index: 92.
    Returns: the total amount of money Sally and Bob will have saved for their trip after a year.
    """

    #: L1
    sally_saved_per_day = sally_daily_wage * fraction_saved # eval: 3.0 = 6 * 0.5

    #: L2
    sally_total_saved = sally_saved_per_day * days_in_year # eval: 1095.0 = 3.0 * 365

    #: L3
    bob_saved_per_day = bob_daily_wage * fraction_saved # eval: 2.0 = 4 * 0.5

    #: L4

    #: L5
    total_saved = sally_total_saved + fraction_saved # eval: 1095.5 = 1095.0 + 0.5

    #: FA
    answer = total_saved
    return answer # eval: return 1095.5
