from fractions import Fraction

def solve():
    """Index: 5230.
    Returns: the total amount of money Tara will have after a year.
    """
    # L1
    interest_rate_numerator = 10 # 10% interest annually
    interest_rate_denominator = 100 # 10% interest annually
    initial_money = 90 # $90 for her birthday
    interest_rate = Fraction(interest_rate_numerator, interest_rate_denominator)
    interest_gained = interest_rate * initial_money

    # L2
    total_money = initial_money + interest_gained

    # FA
    answer = total_money
    return answer