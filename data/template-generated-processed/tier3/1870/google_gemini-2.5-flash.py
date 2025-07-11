def solve():
    """Index: 1870.
    Returns: the angle of B.
    """
    # L1
    total_angle_sum = 180 # WK
    angle_A = 60 # A is 60 degrees
    sum_B_C = total_angle_sum - angle_A

    # L4
    # The solution implies B = 2C, so B + C = 2C + C = 3C. Thus, C = (B+C)/3.
    divisor_for_C = 3 # WK
    angle_C = sum_B_C / divisor_for_C

    # L6
    multiplier_B = 2 # B is two times as big as C
    angle_B = multiplier_B * angle_C

    # FA
    answer = angle_B
    return answer