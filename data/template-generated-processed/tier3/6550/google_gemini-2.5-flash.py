from fractions import Fraction

def solve():
    """Index: 6550.
    Returns: the number of hybrid cars with full headlights.
    """
    # L1
    total_cars = 600 # 600 cars
    hybrid_percentage = Fraction(60, 100) # 60% of the cars are hybrids
    hybrid_cars = hybrid_percentage * total_cars

    # L2
    one_headlight_percentage = Fraction(40, 100) # 40% of the hybrids contain only one headlight
    cars_with_one_headlight = one_headlight_percentage * hybrid_cars

    # L3
    cars_with_full_headlights = hybrid_cars - cars_with_one_headlight

    # FA
    answer = cars_with_full_headlights
    return answer