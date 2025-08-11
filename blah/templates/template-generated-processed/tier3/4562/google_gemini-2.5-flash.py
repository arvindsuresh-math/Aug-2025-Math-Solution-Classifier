from fractions import Fraction

def solve():
    """Index: 4562.
    Returns: the number of holes that remain unfilled.
    """
    # L1
    total_holes = 8 # 8 holes in the lawn
    filled_percentage = Fraction(75, 100) # 75% of the hole
    holes_filled = filled_percentage * total_holes

    # L2
    holes_unfilled = total_holes - holes_filled

    # FA
    answer = holes_unfilled
    return answer