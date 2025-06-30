def solve(
    initial_pink_hard_hats: int = 26, # there are 26 pink hard hats
    initial_green_hard_hats: int = 15, # 15 green hard hats
    initial_yellow_hard_hats: int = 24, # and 24 yellow hard hats
    carl_takes_pink: int = 4, # Carl takes away 4 pink hard hats
    john_takes_pink: int = 6, # John takes away 6 pink hard hats
    john_takes_green_multiplier: int = 2 # and twice as many green hard hats as the number of pink hard hats that he removed
):
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """

    #: L1
    remaining_pink_after_carl = initial_pink_hard_hats - carl_takes_pink

    #: L2
    remaining_pink_after_john = remaining_pink_after_carl - john_takes_pink

    #: L3
    green_john_took = john_takes_pink * john_takes_green_multiplier

    #: L4
    remaining_green_after_john = initial_green_hard_hats - green_john_took

    #: L5
    total_pink_green_remaining = remaining_green_after_john + john_takes_pink

    #: L6
    total_remaining_hard_hats = total_pink_green_remaining + initial_yellow_hard_hats

    #: FA
    answer = total_remaining_hard_hats
    return answer