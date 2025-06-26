def solve(
    pink_hard_hats: int = 26,  # there are 26 pink hard hats
    green_hard_hats: int = 15,  # there are 15 green hard hats
    yellow_hard_hats: int = 24,  # there are 24 yellow hard hats
    carl_pink_taken: int = 4,  # Carl takes away 4 pink hard hats
    john_pink_taken: int = 6  # John takes away 6 pink hard hats
):
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """
    #: L1
    pink_remaining_after_carl = pink_hard_hats - carl_pink_taken

    #: L2
    pink_remaining_after_john = pink_remaining_after_carl - john_pink_taken

    #: L3
    john_green_taken = john_pink_taken * 2

    #: L4
    green_remaining = green_hard_hats - john_green_taken

    #: L5
    pink_and_green_remaining = green_remaining + pink_remaining_after_john

    #: L6
    total_remaining = pink_and_green_remaining + yellow_hard_hats

    answer = total_remaining  # FINAL ANSWER
    return answer