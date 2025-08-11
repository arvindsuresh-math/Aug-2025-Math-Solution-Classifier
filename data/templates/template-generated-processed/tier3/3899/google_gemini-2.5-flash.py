from fractions import Fraction

def solve():
    """Index: 3899.
    Returns: the total number of apples in the box.
    """
    # L1
    total_fruit = 56 # 56 pieces of fruit in a box
    orange_fraction = Fraction(1, 4) # One-fourth of the box contains oranges
    total_oranges = total_fruit * orange_fraction

    # L2
    half_divisor = 2 # half as many peaches as oranges
    total_peaches = total_oranges / half_divisor

    # L3
    apple_multiplier = 5 # five times as many apples as peaches
    total_apples = apple_multiplier * total_peaches

    # FA
    answer = total_apples
    return answer