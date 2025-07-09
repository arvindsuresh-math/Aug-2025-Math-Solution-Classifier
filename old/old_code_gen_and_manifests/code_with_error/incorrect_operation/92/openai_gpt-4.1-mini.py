def solve(
    sally_daily_earnings: int = 6,  # Sally makes $6 per day
    bob_daily_earnings: int = 4,    # Bob makes $4 per day
    days_per_year: int = 365         # each year has 365 days
):
    """Index: 92.
    Returns: the total amount of money Sally and Bob will have saved for their trip after a year.
    """

    #: L1
    sally_daily_savings = 0.5 + sally_daily_earnings

    #: L2
    sally_yearly_savings = sally_daily_savings * days_per_year

    #: L3
    bob_daily_savings = 0.5 * bob_daily_earnings

    #: L4
    bob_yearly_savings = bob_daily_savings * days_per_year

    #: L5
    total_savings = sally_yearly_savings + bob_yearly_savings

    #: FA
    answer = total_savings
    return answer