def solve():
    """Index: 3280.
    Returns: the number of fish Jonah has now.
    """
    # L1
    initial_fish = 14 # started with 14 small fish
    added_fish_initial = 2 # added 2 more
    fish_after_initial_add = initial_fish + added_fish_initial

    # L2
    eaten_fish = 6 # ate 6 of his original fish
    returned_fish = 2 # remove them and take them back to the store
    fish_after_eating_and_return = fish_after_initial_add - eaten_fish - returned_fish

    # L3
    new_fish_exchanged = 3 # exchanged them for 3 new fish
    total_fish = new_fish_exchanged + fish_after_eating_and_return

    # FA
    answer = total_fish
    return answer