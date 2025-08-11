from fractions import Fraction

def solve():
    """Index: 2850.
    Returns: the amount of money Mr. John has left after deducting transport fare.
    """
    # L1
    transport_percentage = Fraction(5, 100) # 5% of this amount
    monthly_income = 2000 # monthly income of $2000
    transport_fare = transport_percentage * monthly_income

    # L2
    remaining_income = monthly_income - transport_fare

    # FA
    answer = remaining_income
    return answer