def solve():
    """Index: 3080.
    Returns: the number of fish Tony will have in five years.
    """
    # L1
    fish_bought_per_year = 2 # his parents buy him two more
    fish_died_per_year = 1 # one of them dies
    net_gain_per_year = fish_bought_per_year - fish_died_per_year

    # L2
    num_years = 5 # in five years
    total_gain_over_years = num_years * net_gain_per_year

    # L3
    initial_fish = 2 # Tony has two fish
    final_fish_count = initial_fish + total_gain_over_years

    # FA
    answer = final_fish_count
    return answer