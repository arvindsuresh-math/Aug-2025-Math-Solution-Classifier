def solve():
    """Index: 17.
    Returns: the total number of hard hats that remained in the truck.
    """
    # L1
    initial_pink = 26 # 26 pink hard hats
    carl_pink_taken = 4 # Carl takes away 4 pink hard hats
    pink_after_carl = initial_pink - carl_pink_taken

    # L2
    john_pink_taken = 6 # John takes away 6 pink hard hats
    pink_after_john = pink_after_carl - john_pink_taken

    # L3
    john_green_multiplier = 2 # twice as many green hard hats as pink hard hats
    john_green_taken = john_pink_taken * john_green_multiplier

    # L4
    initial_green = 15 # 15 green hard hats
    green_after_john = initial_green - john_green_taken

    # L5
    green_and_pink_remaining = green_after_john + pink_after_john

    # L6
    initial_yellow = 24 # 24 yellow hard hats
    total_remaining = green_and_pink_remaining + initial_yellow

    # FA
    answer = total_remaining
    return answer