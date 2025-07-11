from fractions import Fraction

def solve():
    """Index: 1846.
    Returns: the total amount Bob and Kate have to pay after discounts.
    """
    # L1
    bob_bill = 30 # $30 bill to Bob
    bob_discount_percent_numerator = 5 # 5% for Bob
    percent_denominator = 100 # WK
    bob_discount_amount = Fraction(bob_discount_percent_numerator, percent_denominator) * bob_bill

    # L2
    bob_amount_to_pay = bob_bill - bob_discount_amount

    # L3
    kate_bill = 25 # $25 bill to Kate
    kate_discount_percent_numerator = 2 # 2% for Kate
    kate_discount_amount = Fraction(kate_discount_percent_numerator, percent_denominator) * kate_bill

    # L4
    kate_amount_to_pay = kate_bill - kate_discount_amount

    # L5
    total_amount_to_pay = bob_amount_to_pay + kate_amount_to_pay

    # FA
    answer = total_amount_to_pay
    return answer