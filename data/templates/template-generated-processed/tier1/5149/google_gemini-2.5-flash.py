def solve():
    """Index: 5149.
    Returns: the number of fish remaining in the tank.
    """
    # L1
    guppies_initial = 94 # 94 guppies
    angelfish_initial = 76 # 76 angelfish
    tiger_sharks_initial = 89 # 89 tiger sharks
    oscar_fish_initial = 58 # 58 Oscar fish
    total_initial_fish = guppies_initial + angelfish_initial + tiger_sharks_initial + oscar_fish_initial

    # L2
    guppies_sold = 30 # sells 30 guppies
    angelfish_sold = 48 # 48 angelfish
    tiger_sharks_sold = 17 # 17 tiger sharks
    oscar_fish_sold = 24 # 24 Oscar fish
    total_fish_sold = guppies_sold + angelfish_sold + tiger_sharks_sold + oscar_fish_sold

    # L3
    remaining_fish = total_initial_fish - total_fish_sold

    # FA
    answer = remaining_fish
    return answer