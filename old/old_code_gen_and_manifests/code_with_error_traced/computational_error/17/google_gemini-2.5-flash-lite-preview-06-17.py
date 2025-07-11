def solve(
    initial_pink_hats: int = 26, # there are 26 pink hard hats
    initial_green_hats: int = 15, # 15 green hard hats
    initial_yellow_hats: int = 24, # and 24 yellow hard hats
    carl_takes_pink: int = 4, # Carl takes away 4 pink hard hats
    john_takes_pink: int = 6, # John takes away 6 pink hard hats
):
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """

    #: L1
    remaining_pink_after_carl = initial_pink_hats - carl_takes_pink # eval: 22 = 26 - 4

    #: L2
    remaining_pink_after_john = remaining_pink_after_carl - john_takes_pink # eval: 16 = 22 - 6

    #: L3
    john_takes_green = 22 # eval: 22 = 22

    #: L4
    remaining_green = initial_green_hats - john_takes_green # eval: -7 = 15 - 22

    #: L5
    remaining_pink_and_green = remaining_pink_after_john + remaining_green # eval: 9 = 16 + -7

    #: L6
    total_remaining_hats = remaining_pink_and_green + initial_yellow_hats # eval: 33 = 9 + 24

    #: FA
    answer = total_remaining_hats
    return answer # eval: return 33
