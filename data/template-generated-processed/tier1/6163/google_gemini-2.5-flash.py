def solve():
    """Index: 6163.
    Returns: the value of the top angle.
    """
    # L1
    right_angle_value = 60 # the right angle is 60 degrees
    multiplier_for_left_angle = 2 # twice the right angle's value
    left_angle = right_angle_value * multiplier_for_left_angle

    # L2
    sum_left_right_angles = left_angle + right_angle_value

    # L3
    sum_three_angles = 250 # The sum of the three angles of a triangle equals 250
    top_angle = sum_three_angles - sum_left_right_angles

    # FA
    answer = top_angle
    return answer