from fractions import Fraction

def solve():
    """Index: 29.
    Returns: Mrs. Snyder's previous monthly income.
    """
    # L2
    rent_utilities_percent_old = Fraction(40, 100) # 40% of her monthly income on rent and utilities
    # Let her previous monthly income be p (unknown)
    # cost_old = rent_utilities_percent_old * p
    # 2p/5 is equivalent to (2/5)*p, which is 40% of p
    # L3
    salary_increase = 600 # salary was recently increased by $600
    # new_income = p + salary_increase
    # L4
    rent_utilities_percent_new = Fraction(25, 100) # 25% of her monthly income
    # cost_new = rent_utilities_percent_new * (p + salary_increase)
    # (p + salary_increase)/4 is equivalent to 25% of (p + $600)
    # L5
    # Equate both expressions: (2/5)*p = (p + 600)/4
    # L6
    # Multiply both sides by 20: 20*(2/5)*p = 20*(p + 600)/4
    # 8p = 5p + 3000
    # L7
    # 8p - 5p = 3000
    # 3p = 3000
    # L8
    previous_income = 3000 / 3
    # FA
    answer = previous_income
    return answer