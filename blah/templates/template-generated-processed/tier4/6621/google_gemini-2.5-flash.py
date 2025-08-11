from fractions import Fraction

def solve():
    """Index: 6621.
    Returns: the total number of complaints the store gets.
    """
    # L1
    normal_complaints_per_day = 120 # 120 customer complaints per day
    short_staffed_increase_factor = Fraction(4, 3) # increases by 1/3rd
    complaints_short_staffed = normal_complaints_per_day * short_staffed_increase_factor

    # L2
    self_checkout_broken_increase_factor = 1.2 # increases by another 20%
    complaints_broken_checkout = complaints_short_staffed * self_checkout_broken_increase_factor

    # L3
    num_days = 3 # for 3 days
    total_complaints = complaints_broken_checkout * num_days

    # FA
    answer = total_complaints
    return answer