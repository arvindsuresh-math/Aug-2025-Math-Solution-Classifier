def solve(
        fraction_saved: float = 0.5, # save half of what they've earned
        sally_daily_earnings: int = 6, # Sally makes $6 per day
        bob_daily_earnings: int = 4, # Bob makes $4 per day
        days_in_year: int = 365 # after a year (implied)
    ):
    """Index: 92.
    Returns: the total amount of money Sally and Bob will have saved for their trip after a year.
    """

    #: L1
    sally_daily_savings = fraction_saved * sally_daily_earnings # eval: 3.0 = 0.5 * 6

    #: L2
    sally_yearly_savings = sally_daily_savings * days_in_year # eval: 1095.0 = 3.0 * 365

    #: L3
    bob_daily_savings = fraction_saved * bob_daily_earnings # eval: 2.0 = 0.5 * 4

    #: L4
    bob_yearly_savings = bob_daily_savings * days_in_year # eval: 730.0 = 2.0 * 365

    #: L5
    total_saved = bob_yearly_savings + sally_yearly_savings # eval: 1825.0 = 730.0 + 1095.0

    #: FA
    answer = total_saved
    return answer # eval: return 1825.0
