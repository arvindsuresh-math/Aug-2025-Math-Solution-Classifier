from fractions import Fraction

def solve():
    """Index: 2757.
    Returns: the total amount of money in Fernanda's savings account.
    """
    # L1
    aryan_debt = 1200 # Aryan owes Fernanda $1200
    half_fraction = Fraction(1, 2) # twice what Kyro owes Fernanda
    kyro_debt = half_fraction * aryan_debt

    # L2
    aryan_payment_percentage = Fraction(60, 100) # 60% of her debt
    aryan_payment = aryan_payment_percentage * aryan_debt

    # L3
    initial_savings = 300 # Fernanda had $300 in her savings account
    savings_after_aryan_payment = initial_savings + aryan_payment

    # L4
    kyro_payment_percentage = Fraction(80, 100) # 80% of her dept
    kyro_payment = kyro_payment_percentage * kyro_debt

    # L5
    final_savings = savings_after_aryan_payment + kyro_payment

    # FA
    answer = final_savings
    return answer