from fractions import Fraction

def solve():
    """Index: 6697.
    Returns: the number of months Renne needs to save.
    """
    # L1
    saving_fraction = Fraction(1, 2) # half of her monthly earnings
    monthly_earnings = 4000 # $4000 per month
    monthly_savings = saving_fraction * monthly_earnings

    # L2
    vehicle_cost = 16000 # worth $16000
    months_to_save = vehicle_cost / monthly_savings

    # FA
    answer = months_to_save
    return answer