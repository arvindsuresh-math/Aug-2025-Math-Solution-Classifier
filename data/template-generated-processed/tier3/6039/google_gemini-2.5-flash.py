from fractions import Fraction

def solve():
    """Index: 6039.
    Returns: the loss incurred by the hotel.
    """
    # L1
    payment_fraction = Fraction(3, 4) # 3/4 of the cost
    operations_expenses = 100 # operations expenses totaling $100
    total_payment = payment_fraction * operations_expenses

    # L2
    loss_incurred = operations_expenses - total_payment

    # FA
    answer = loss_incurred
    return answer