def solve():
    """Index: 7062.
    Returns: the total number of fish caught by all three.
    """
    # L1
    jeffery_fish = 60 # Jeffery caught 60 fish
    ryan_multiplier = 2 # twice the number of fish that Ryan got
    ryan_fish = jeffery_fish / ryan_multiplier

    # L2
    jason_multiplier = 3 # three times the number of fish that Jason caught
    jason_fish = ryan_fish / jason_multiplier

    # L3
    total_fish = jason_fish + ryan_fish + jeffery_fish

    # FA
    answer = total_fish
    return answer