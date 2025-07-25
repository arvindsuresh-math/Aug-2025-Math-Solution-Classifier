from fractions import Fraction

def solve():
    """Index: 4259.
    Returns: the number of sweets the second child gets.
    """
    # L1
    total_sweets = 27 # 27 pieces of sweets in the box
    mother_kept_fraction = Fraction(1, 3) # 1/3 of the sweets
    sweets_mother_kept = total_sweets * mother_kept_fraction

    # L2
    sweets_for_children = total_sweets - sweets_mother_kept

    # L3
    eldest_sweets = 8 # The eldest got 8 sweets
    half_divisor = 2 # half as many
    youngest_sweets = eldest_sweets / half_divisor

    # L4
    eldest_and_youngest_total = eldest_sweets + youngest_sweets

    # L5
    second_child_sweets = sweets_for_children - eldest_and_youngest_total

    # FA
    answer = second_child_sweets
    return answer