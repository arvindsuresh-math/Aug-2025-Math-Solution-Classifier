def solve():
    """Index: 5742.
    Returns: the total length of Jazel's sticks.
    """
    # L1
    first_stick_length = 3 # One stick is 3 centimeters long
    multiplier_for_second_stick = 2 # twice as long
    second_stick_length = first_stick_length * multiplier_for_second_stick

    # L2
    shorter_than_second_stick = 1 # 1 centimeter shorter
    third_stick_length = second_stick_length - shorter_than_second_stick

    # L3
    total_length = first_stick_length + second_stick_length + third_stick_length

    # FA
    answer = total_length
    return answer