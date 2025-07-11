from fractions import Fraction

def solve():
    """Index: 1272.
    Returns: Ruiz's new salary after the raise.
    """
    # L1
    initial_salary = 500 # monthly salary of $500
    raise_percentage = Fraction(6, 100) # 6% raise
    salary_raise = initial_salary * raise_percentage

    # L2
    new_salary = initial_salary + salary_raise

    # FA
    answer = new_salary
    return answer