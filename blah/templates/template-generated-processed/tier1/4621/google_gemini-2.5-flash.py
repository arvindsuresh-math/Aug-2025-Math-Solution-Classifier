def solve():
    """Index: 4621.
    Returns: the total number of strings John needs.
    """
    # L1
    num_basses = 3 # 3 basses
    strings_per_bass = 4 # 4 strings each
    basses_strings = num_basses * strings_per_bass

    # L2
    multiplier_normal_guitars = 2 # twice as many guitars
    num_normal_guitars = multiplier_normal_guitars * num_basses

    # L3
    strings_per_normal_guitar = 6 # 6 strings each
    normal_guitars_strings = num_normal_guitars * strings_per_normal_guitar

    # L4
    fewer_8_string_guitars = 3 # 3 fewer 8 string guitars
    num_8_string_guitars = num_normal_guitars - fewer_8_string_guitars

    # L5
    strings_per_8_string_guitar = 8 # 8 string guitars
    eight_string_guitars_strings = num_8_string_guitars * strings_per_8_string_guitar

    # L6
    total_strings = basses_strings + normal_guitars_strings + eight_string_guitars_strings

    # FA
    answer = total_strings
    return answer