from fractions import Fraction

def solve():
    """Index: 92.
    Returns: the total money saved by Sally and Bob for their trip.
    """
    # L1
    saving_fraction = Fraction(1, 2) # save half of what they've earned
    sally_daily_rate = 6 # Sally makes $6 per day
    sally_daily_savings = saving_fraction * sally_daily_rate

    # L2
    days_per_year = 365 # Since each year have 365 days
    sally_yearly_savings = sally_daily_savings * days_per_year

    # L3
    bob_daily_rate = 4 # Bob makes $4 per day
    bob_daily_savings = saving_fraction * bob_daily_rate

    # L4
    bob_yearly_savings = bob_daily_savings * days_per_year

    # L5
    total_saved = bob_yearly_savings + sally_yearly_savings

    # FA
    answer = total_saved
    return answer