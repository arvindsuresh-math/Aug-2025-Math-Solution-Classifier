def solve():
    """Index: 2709.
    Returns: the number of people in Class C.
    """
    # L2
    class_b_size = 20 # Class B has 20 people in it
    class_a_multiplier = 2 # Class A is twice as big as Class B
    class_a_size = class_b_size * class_a_multiplier

    # L5
    class_c_multiplier = 3 # Class A is also a third the size of Class C
    class_c_size = class_c_multiplier * class_a_size

    # FA
    answer = class_c_size
    return answer