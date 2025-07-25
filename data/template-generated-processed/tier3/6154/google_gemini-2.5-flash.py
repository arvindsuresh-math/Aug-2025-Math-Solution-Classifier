def solve():
    """Index: 6154.
    Returns: the number of characters with the initial D.
    """
    # L1
    total_characters = 60 # 60 characters
    half_divisor = 2 # Half of her characters
    characters_initial_A = total_characters / half_divisor

    # L2
    characters_initial_C = characters_initial_A / half_divisor

    # L3
    remaining_characters_D_E = total_characters - characters_initial_A - characters_initial_C

    # L4
    ratio_D = 2 # twice as many characters with the initial D
    ratio_E = 1 # twice as many characters with the initial D as there are characters with the initial E
    total_parts = ratio_D + ratio_E

    # L5
    characters_initial_E = remaining_characters_D_E / total_parts

    # L6
    characters_initial_D = remaining_characters_D_E - characters_initial_E

    # FA
    answer = characters_initial_D
    return answer