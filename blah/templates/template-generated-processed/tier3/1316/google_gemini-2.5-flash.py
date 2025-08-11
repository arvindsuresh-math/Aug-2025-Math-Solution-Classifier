from fractions import Fraction

def solve():
    """Index: 1316.
    Returns: the number of pizza slices James ate.
    """
    # L1
    num_pizzas = 2 # 2 small pizzas
    slices_per_pizza = 6 # Each pizza has 6 slices
    total_slices = num_pizzas * slices_per_pizza

    # L2
    james_fraction = Fraction(2, 3) # James ate 2/3 of all the slices
    james_ate_slices = james_fraction * total_slices

    # FA
    answer = james_ate_slices
    return answer