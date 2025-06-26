def solve(
        savings_fraction: float = 0.5, # save half of what they've earned
        sally_daily_earnings: int = 6, # Sally makes $6 per day
        bob_daily_earnings: int = 4, # Bob makes $4 per day
        days_in_year: int = 365 # after a year (implied 365 days)
    ):
    """Index: 92.
    Returns: the total amount of money Sally and Bob will have saved for their trip after a year.
    """
    #: L1
    sally_daily_savings = savings_fraction * sally_daily_earnings

    #: L2
    sally_yearly_savings = sally_daily_savings * days_in_year

    #: L3
    bob_daily_savings = savings_fraction * bob_daily_earnings

    #: L4
    bob_yearly_savings = bob_daily_savings * days_in_year

    #: L5
    total_saved = bob_yearly_savings + sally_yearly_savings

    answer = total_saved # FINAL ANSWER
    return answer