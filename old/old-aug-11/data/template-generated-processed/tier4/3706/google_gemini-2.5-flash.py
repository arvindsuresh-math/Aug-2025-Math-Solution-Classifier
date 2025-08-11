from fractions import Fraction

def solve():
    """Index: 3706.
    Returns: the final amount left in Bobby's paycheck in dollars.
    """
    # L1
    federal_tax_fraction = Fraction(1, 3) # 1/3 in federal taxes
    salary_per_week = 450 # salary is $450 per week
    federal_tax_amount = federal_tax_fraction * salary_per_week

    # L2
    state_tax_rate = 0.08 # 8% in state taxes
    state_tax_amount = state_tax_rate * salary_per_week

    # L3
    health_insurance = 50 # $50 per week
    life_insurance = 20 # $20 per week
    parking_fee = 10 # $10 per week for parking
    final_paycheck_amount = salary_per_week - federal_tax_amount - state_tax_amount - health_insurance - life_insurance - parking_fee

    # FA
    answer = final_paycheck_amount
    return answer