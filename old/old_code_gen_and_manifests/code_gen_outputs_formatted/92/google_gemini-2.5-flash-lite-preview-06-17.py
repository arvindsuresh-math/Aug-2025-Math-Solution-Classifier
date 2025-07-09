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
    sally_saved_per_day = sally_daily_wage * fraction_saved

    #: L2
    sally_total_saved = sally_saved_per_day * days_in_year

    #: L3
    bob_saved_per_day = bob_daily_wage * fraction_saved

    #: L4
    bob_total_saved = bob_saved_per_day * days_in_year

    #: L5
    total_saved = sally_total_saved + bob_total_saved

    #: FA
    answer = total_saved
    return answer