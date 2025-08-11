from fractions import Fraction

def solve():
    """Index: 7220.
    Returns: the amount of money Donny spent.
    """
    # L1
    monday_savings = 15 # $15 on Monday
    tuesday_savings = 28 # $28 on Tuesday
    wednesday_savings = 13 # $13 on Wednesday
    total_savings_three_days = monday_savings + tuesday_savings + wednesday_savings

    # L2
    half_fraction = Fraction(1, 2) # half of his total savings
    amount_spent = total_savings_three_days * half_fraction

    # FA
    answer = amount_spent
    return answer