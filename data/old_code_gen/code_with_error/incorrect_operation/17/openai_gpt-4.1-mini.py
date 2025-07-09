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
    pink_after_carl = pink_hard_hats - carl_pink_taken

    #: L2
    pink_after_john = pink_after_carl + john_pink_taken

    #: L3
    john_green_taken = john_pink_taken * 2

    #: L4
    green_after_john = green_hard_hats - john_green_taken

    #: L5
    pink_green_total = green_after_john + pink_after_john

    #: L6
    total_remaining = pink_green_total + yellow_hard_hats

    #: FA
    answer = total_remaining
    return answer