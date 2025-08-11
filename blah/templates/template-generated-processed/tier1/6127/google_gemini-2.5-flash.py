def solve():
    """Index: 6127.
    Returns: the thickness of the blanket after 4 foldings.
    """
    # L1
    initial_thickness = 3 # starts out 3 inches thick
    doubling_factor = 2 # thickness doubles
    thickness_after_1_folding = initial_thickness * doubling_factor

    # L2
    thickness_after_2_foldings = thickness_after_1_folding * doubling_factor

    # L3
    thickness_after_3_foldings = thickness_after_2_foldings * doubling_factor

    # L4
    thickness_after_4_foldings = thickness_after_3_foldings * doubling_factor

    # FA
    answer = thickness_after_4_foldings
    return answer