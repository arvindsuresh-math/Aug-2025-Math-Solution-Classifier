from fractions import Fraction

def solve():
    """Index: 7428.
    Returns: the number of toy cars Gerald has left.
    """
    # L1
    total_cars = 20 # 20 toy cars
    donated_fraction = Fraction(1, 4) # 1/4 of his toy cars
    cars_donated = total_cars * donated_fraction

    # L2
    cars_left = total_cars - cars_donated

    # FA
    answer = cars_left
    return answer