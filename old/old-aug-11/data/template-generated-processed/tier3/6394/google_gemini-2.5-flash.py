from fractions import Fraction

def solve():
    """Index: 6394.
    Returns: the number of successfully inflated soccer balls.
    """
    # L1
    total_balls = 100 # Of the 100 soccer balls
    holes_percentage = Fraction(40, 100) # 40 percent had holes in them
    balls_with_holes = holes_percentage * total_balls

    # L2
    remaining_balls_after_holes = total_balls - balls_with_holes

    # L3
    overinflated_percentage = Fraction(20, 100) # 20% of the remaining balls were overinflated
    overinflated_balls = overinflated_percentage * remaining_balls_after_holes

    # L4
    successfully_inflated_balls = remaining_balls_after_holes - overinflated_balls

    # FA
    answer = successfully_inflated_balls
    return answer