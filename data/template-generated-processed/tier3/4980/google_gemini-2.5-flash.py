from fractions import Fraction

def solve():
    """Index: 4980.
    Returns: the total number of marbles both bowls are holding together.
    """
    # L1
    first_bowl_capacity_fraction = Fraction(3, 4) # 3/4 the capacity of the second bowl
    second_bowl_marbles = 600 # second bowl has 600 marbles
    first_bowl_marbles = first_bowl_capacity_fraction * second_bowl_marbles

    # L2
    total_marbles = first_bowl_marbles + second_bowl_marbles

    # FA
    answer = total_marbles
    return answer