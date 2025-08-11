from fractions import Fraction

def solve():
    """Index: 92.
    Returns: the total amount Sally and Bob will have saved for their trip after a year.
    """
    # L1
    sally_save_fraction = Fraction(1, 2) # save half of what they've earned
    sally_daily_earnings = 6 # Sally makes $6 per day
    sally_daily_savings = sally_save_fraction * sally_daily_earnings

    # L2
    days_per_year = 365 # each year have 365 days
    sally_yearly_savings = sally_daily_savings * days_per_year

    # L3
    bob_save_fraction = Fraction(1, 2) # save half of what they've earned
    bob_daily_earnings = 4 # Bob makes $4 per day
    bob_daily_savings = bob_save_fraction * bob_daily_earnings

    # L4
    bob_yearly_savings = bob_daily_savings * days_per_year

    # L5
    total_savings = bob_yearly_savings + sally_yearly_savings

    # FA
    answer = total_savings
    return answer