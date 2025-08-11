def solve():
    """Index: 452.
    Returns: the number of marbles Emily has now.
    """
    # L1
    emily_initial_marbles = 6 # Emily has 6 marbles
    double_factor = 2 # double the number she has
    marbles_megan_gives = emily_initial_marbles * double_factor

    # L2
    emily_total_after_receiving = emily_initial_marbles + marbles_megan_gives

    # L3
    half_divisor = 2 # half of her new total
    additional_given = 1 # plus 1
    marbles_emily_gives_back = emily_total_after_receiving / half_divisor + additional_given

    # L4
    emily_final_marbles = emily_total_after_receiving - marbles_emily_gives_back

    # FA
    answer = emily_final_marbles
    return answer