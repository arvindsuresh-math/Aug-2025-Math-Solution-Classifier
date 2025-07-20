from fractions import Fraction

def solve():
    """Index: 4643.
    Returns: the total amount of money to be paid back.
    """
    # L1
    borrowed_amount = 100 # borrowed $100 from your friend
    increase_percentage_numerator = 10 # 10% increase
    increase_percentage_denominator = 100 # 10% increase
    increase_amount = borrowed_amount * Fraction(increase_percentage_numerator, increase_percentage_denominator)

    # L2
    total_payment = borrowed_amount + increase_amount

    # FA
    answer = total_payment
    return answer