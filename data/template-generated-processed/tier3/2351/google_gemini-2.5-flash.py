from fractions import Fraction

def solve():
    """Index: 2351.
    Returns: Lanie's salary for that week.
    """
    # L1
    usual_hours_per_week = 40 # usual 40-hour week
    fraction_worked = Fraction(4, 5) # 4/5 of her usual
    hours_worked = usual_hours_per_week * fraction_worked

    # L2
    hourly_rate = 15 # hourly rate is $15
    salary = hourly_rate * hours_worked

    # FA
    answer = salary
    return answer