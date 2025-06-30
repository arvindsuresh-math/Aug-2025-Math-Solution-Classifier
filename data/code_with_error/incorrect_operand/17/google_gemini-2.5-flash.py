def solve(
        initial_pink_hard_hats: int = 26, # there are 26 pink hard hats
        initial_green_hard_hats: int = 15, # 15 green hard hats
        initial_yellow_hard_hats: int = 24, # and 24 yellow hard hats
        carl_removed_pink: int = 4, # Carl takes away 4 pink hard hats
        john_removed_pink: int = 6 # John takes away 6 pink hard hats
    ):
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """

    #: L1
    pink_hats_after_carl = initial_pink_hard_hats - carl_removed_pink

    #: L2
    pink_hats_after_john = pink_hats_after_carl - john_removed_pink

    #: L3
    john_removed_green = john_removed_pink * 2

    #: L4
    remaining_green_hats = initial_green_hard_hats - pink_hats_after_john

    #: L5
    remaining_pink_and_green_hats = remaining_green_hats + pink_hats_after_john

    #: L6
    total_remaining_hard_hats = remaining_pink_and_green_hats + initial_yellow_hard_hats

    #: FA
    answer = total_remaining_hard_hats
    return answer