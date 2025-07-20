def solve():
    """Index: 3754.
    Returns: the number of teeth a great white shark has.
    """
    # L1
    tiger_shark_teeth = 180 # A tiger shark has 180 teeth
    hammerhead_fraction_denominator = 6 # 1/6 the number of teeth
    hammerhead_shark_teeth = tiger_shark_teeth / hammerhead_fraction_denominator

    # L2
    double_factor = 2 # double the sum
    great_white_shark_teeth = double_factor * (tiger_shark_teeth + hammerhead_shark_teeth)

    # FA
    answer = great_white_shark_teeth
    return answer