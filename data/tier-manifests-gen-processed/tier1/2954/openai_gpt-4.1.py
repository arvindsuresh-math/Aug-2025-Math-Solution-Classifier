def solve():
    """Index: 2954.
    Returns: the number of spaces in section 2 of the parking lot.
    """
    # L1
    total_spaces = 1000 # A 1000 car parking lot
    section1_spaces = 320 # 320 spaces in section 1
    remaining_spaces = total_spaces - section1_spaces

    # L5
    # From L3 and L4: 320 + x + 200 + x = 1000 => 2x = 480 => x = 240
    section3_spaces = 240 # x = 240

    # L6
    section2_more_than_3 = 200 # 200 more in section 2 than in section 3
    section2_spaces = section3_spaces + section2_more_than_3

    # FA
    answer = section2_spaces
    return answer