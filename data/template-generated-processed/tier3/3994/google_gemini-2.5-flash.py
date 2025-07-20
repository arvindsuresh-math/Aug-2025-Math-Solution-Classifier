from fractions import Fraction

def solve():
    """Index: 3994.
    Returns: the number of miniature racing cars left with Tom.
    """
    # L1
    num_packages = 10 # 10 packages of miniature racing cars
    cars_per_package = 5 # Each package contains five cars
    total_cars = num_packages * cars_per_package

    # L2
    fraction_given_per_nephew = Fraction(1, 5) # 1/5 of the cars
    cars_given_per_nephew = total_cars * fraction_given_per_nephew

    # L3
    num_nephews = 2 # two nephews
    total_cars_given = cars_given_per_nephew * num_nephews

    # L4
    remaining_cars = total_cars - total_cars_given

    # FA
    answer = remaining_cars
    return answer