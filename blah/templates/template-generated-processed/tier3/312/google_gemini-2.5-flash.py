def solve():
    """Index: 312.
    Returns: the number of emus in the flock.
    """
    # L1
    emu_heads = 1 # WK
    emu_legs = 2 # WK
    total_parts_per_emu = emu_heads + emu_legs

    # L2
    total_heads_and_legs = 60 # His flock has a total of 60 heads and legs
    number_of_emus = total_heads_and_legs / total_parts_per_emu

    # FA
    answer = number_of_emus
    return answer