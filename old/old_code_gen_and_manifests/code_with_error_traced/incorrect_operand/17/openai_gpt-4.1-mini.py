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
    pink_after_carl = pink_hard_hats - carl_pink_taken # eval: 22 = 26 - 4

    #: L2
    pink_after_john = pink_after_carl - john_pink_taken # eval: 16 = 22 - 6

    #: L3
    john_green_taken = green_hard_hats * 2 # eval: 30 = 15 * 2

    #: L4
    green_after_john = green_hard_hats - john_green_taken # eval: -15 = 15 - 30

    #: L5
    pink_green_total = green_after_john + pink_after_john # eval: 1 = -15 + 16

    #: L6
    total_remaining = pink_green_total + yellow_hard_hats # eval: 25 = 1 + 24

    #: FA
    answer = total_remaining
    return answer # eval: return 25
