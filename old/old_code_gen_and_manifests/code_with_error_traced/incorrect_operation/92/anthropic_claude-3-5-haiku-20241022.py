def solve(
        sally_daily_rate: int = 6,  # Sally makes $6 per day
        bob_daily_rate: int = 4,  # Bob makes $4 per day
        savings_fraction: float = 0.5,  # They both decide to save half of what they've earned
        days_in_year: int = 365  # Number of days in a year
    ):
    """Index: 92.
    Returns: the total amount of money Sally and Bob will save for their trip in a year.
    """

    #: L1
    sally_daily_savings = sally_daily_rate - savings_fraction # eval: 5.5 = 6 - 0.5

    #: L2
    sally_yearly_savings = sally_daily_savings * days_in_year # eval: 2007.5 = 5.5 * 365

    #: L3
    bob_daily_savings = bob_daily_rate * savings_fraction # eval: 2.0 = 4 * 0.5

    #: L4
    bob_yearly_savings = bob_daily_savings * days_in_year # eval: 730.0 = 2.0 * 365

    #: L5
    total_savings = sally_yearly_savings + bob_yearly_savings # eval: 2737.5 = 2007.5 + 730.0

    #: FA
    answer = total_savings
    return answer # eval: return 2737.5
