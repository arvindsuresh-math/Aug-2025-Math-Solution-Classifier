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

    #: L2
    pink_hats_after_john = carl_removed_pink - john_removed_pink # eval: -2 = 4 - 6

    #: L3
    john_removed_green = john_removed_pink * 2 # eval: 12 = 6 * 2

    #: L4
    remaining_green_hats = initial_green_hard_hats - john_removed_green # eval: 3 = 15 - 12

    #: L5
    remaining_pink_and_green_hats = remaining_green_hats + pink_hats_after_john # eval: 1 = 3 + -2

    #: L6
    total_remaining_hard_hats = remaining_pink_and_green_hats + initial_yellow_hard_hats # eval: 25 = 1 + 24

    #: FA
    answer = total_remaining_hard_hats
    return answer # eval: return 25
