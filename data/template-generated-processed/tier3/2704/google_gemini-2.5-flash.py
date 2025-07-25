from fractions import Fraction

def solve():
    """Index: 2704.
    Returns: the current value of the car.
    """
    # L1
    initial_value = 4000 # Jocelyn bought a car 3 years ago at $4000
    reduction_percentage = Fraction(30, 100) # reduced by 30%
    value_reduction = reduction_percentage * initial_value

    # L2
    current_value = initial_value - value_reduction

    # FA
    answer = current_value
    return answer