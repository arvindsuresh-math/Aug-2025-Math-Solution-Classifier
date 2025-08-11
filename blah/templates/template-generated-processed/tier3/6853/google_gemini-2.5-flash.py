from fractions import Fraction

def solve():
    """Index: 6853.
    Returns: the amount of a monthly payment.
    """
    # L1
    original_price = 480 # new television for $480
    discount_percentage = Fraction(5, 100) # a 5% discount
    discount_amount = original_price * discount_percentage

    # L2
    price_after_discount = original_price - discount_amount

    # L3
    first_installment = 150 # pay a first installment of $150
    outstanding_balance = price_after_discount - first_installment

    # L4
    num_monthly_installments = 3 # will pay the rest in 3 monthly installments
    monthly_payment_amount = outstanding_balance / num_monthly_installments

    # FA
    answer = monthly_payment_amount
    return answer