def solve():
    """Index: 4707.
    Returns: the total number of fish in the lake.
    """
    # L1
    fish_per_white_duck = 5 # 5 fish
    num_white_ducks = 3 # 3 white ducks
    total_fish_white_ducks = fish_per_white_duck * num_white_ducks

    # L2
    fish_per_black_duck = 10 # 10 fish
    num_black_ducks = 7 # 7 black ducks
    total_fish_black_ducks = fish_per_black_duck * num_black_ducks

    # L3
    fish_per_multicolor_duck = 12 # 12 fish
    num_multicolor_ducks = 6 # 6 multicolored ducks
    total_fish_multicolor_ducks = fish_per_multicolor_duck * num_multicolor_ducks

    # L4
    total_fish_in_lake = total_fish_white_ducks + total_fish_black_ducks + total_fish_multicolor_ducks

    # FA
    answer = total_fish_in_lake
    return answer