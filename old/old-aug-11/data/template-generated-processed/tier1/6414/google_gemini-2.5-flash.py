def solve():
    """Index: 6414.
    Returns: the total number of flies eaten every day in the swamp.
    """
    # L1
    num_gharials = 9 # it has 9 gharials
    fish_per_gharial = 15 # eat 15 fish a day
    total_fish_eaten = num_gharials * fish_per_gharial

    # L2
    frogs_per_fish = 8 # eat 8 frogs per day
    total_frogs_eaten = total_fish_eaten * frogs_per_fish

    # L3
    flies_per_frog = 30 # eat 30 flies per day
    total_flies_eaten = total_frogs_eaten * flies_per_frog

    # FA
    answer = total_flies_eaten
    return answer