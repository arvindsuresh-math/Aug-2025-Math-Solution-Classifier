def solve():
    """Index: 988.
    Returns: the volume of the box.
    """
    # L1
    height = 12 # 12 inches in height
    length_multiplier = 3 # 3 times its height
    length = length_multiplier * height

    # L2
    width_divisor = 4 # 4 times its width
    width = length / width_divisor

    # L3
    volume = height * length * width

    # FA
    answer = volume
    return answer