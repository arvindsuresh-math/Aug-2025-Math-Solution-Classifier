from fractions import Fraction

def solve():
    """Index: 66.
    Returns: Tara's remaining balance after 4 months of payments.
    """
    # L1
    laptop_cost = 1000 # laptop which costs $1000
    down_payment_percentage = Fraction(20, 100) # 20% down payment
    initial_down_payment = laptop_cost * down_payment_percentage

    # L2
    additional_down_payment = 20 # pay an additional $20 for the down payment
    total_down_payment = initial_down_payment + additional_down_payment

    # L3
    remaining_balance_initial = laptop_cost - total_down_payment

    # L4
    months_per_year = 12 # WK
    monthly_payment_calculated = remaining_balance_initial / months_per_year

    # L5
    number_of_months_paid = 4 # after paying for 4 months
    total_payments_for_4_months = monthly_payment_calculated * number_of_months_paid

    # L6
    final_balance = remaining_balance_initial - total_payments_for_4_months

    # FA
    answer = final_balance
    return answer