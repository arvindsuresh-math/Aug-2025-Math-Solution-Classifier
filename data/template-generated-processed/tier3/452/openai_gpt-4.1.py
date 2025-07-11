def solve():
    """Index: 452.
    Returns: the number of marbles Emily has now.
    """
    # L1
    emily_initial_marbles = 6 # Emily has 6 marbles
    megan_gives_multiplier = 2 # Megan gives Emily double the number she has
    megan_gives = emily_initial_marbles * megan_gives_multiplier

    # L2
    emily_after_gift = emily_initial_marbles + megan_gives

    # L3
    give_back_divisor = 2 # half of her new total
    give_back_extra = 1 # plus 1
    emily_gives_back = emily_after_gift / give_back_divisor + give_back_extra

    # L4
    emily_final_marbles = emily_after_gift - emily_gives_back

    # FA
    answer = emily_final_marbles
    return answer