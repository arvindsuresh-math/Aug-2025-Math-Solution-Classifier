def solve(
        pink_hard_hats_initial: int = 26, # there are 26 pink hard hats
        green_hard_hats_initial: int = 15, # 15 green hard hats
        yellow_hard_hats_initial: int = 24, # and 24 yellow hard hats
        carl_takes_pink: int = 4, # Carl takes away 4 pink hard hats
        john_takes_pink: int = 6 # John takes away 6 pink hard hats
    ):
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """
    #: L1
    pink_hard_hats_after_carl = pink_hard_hats_initial - carl_takes_pink

    #: L2
    pink_hard_hats_after_john = pink_hard_hats_after_carl - john_takes_pink

    #: L3
    john_takes_green = john_takes_pink * 2

    #: L4
    green_hard_hats_remaining = green_hard_hats_initial - john_takes_green

    #: L5
    pink_and_green_remaining = green_hard_hats_remaining + pink_hard_hats_after_john

    #: L6
    total_hard_hats_remaining = pink_and_green_remaining + yellow_hard_hats_initial

    answer = total_hard_hats_remaining # FINAL ANSWER
    return answer