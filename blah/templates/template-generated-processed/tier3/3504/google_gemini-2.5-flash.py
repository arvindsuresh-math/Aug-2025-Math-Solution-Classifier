from fractions import Fraction

def solve():
    """Index: 3504.
    Returns: the total number of bricks the wall has.
    """
    # L1
    initial_courses = 3 # three courses of bricks
    added_courses = 2 # added 2 more courses
    total_courses = initial_courses + added_courses

    # L2
    bricks_per_course = 400 # each course of the wall had 400 bricks
    total_bricks_before_removal = total_courses * bricks_per_course

    # L3
    removed_fraction = Fraction(1, 2) # half of the bricks
    bricks_removed = removed_fraction * bricks_per_course

    # L4
    final_total_bricks = total_bricks_before_removal - bricks_removed

    # FA
    answer = final_total_bricks
    return answer