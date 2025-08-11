def solve():
    """Index: 6804.
    Returns: the value of the triangle base.
    """
    # L1
    left_side_length = 12 # left side has a value of 12 cm
    right_side_longer_than_left = 2 # right side of the triangle is 2 cm longer than the left side
    right_side_length = left_side_length + right_side_longer_than_left

    # L2
    sum_left_right_sides = right_side_length + left_side_length

    # L3
    total_sum_sides = 50 # The sum of the three sides of a triangle is 50
    triangle_base = total_sum_sides - sum_left_right_sides

    # FA
    answer = triangle_base
    return answer