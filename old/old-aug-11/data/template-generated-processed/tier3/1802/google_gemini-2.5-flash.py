def solve():
    """Index: 1802.
    Returns: the total number of fish Jason has.
    """
    # L1
    initial_fish = 6 # Jason has six fish
    doubling_factor = 2 # the number of fish doubles
    fish_day_3_before_removal = initial_fish * doubling_factor * doubling_factor

    # L2
    removal_divisor_day_3 = 3 # one-third of the fish
    fish_removed_day_3 = fish_day_3_before_removal / removal_divisor_day_3

    # L3
    fish_end_day_3 = fish_day_3_before_removal - fish_removed_day_3

    # L4
    fish_day_5_before_removal = fish_end_day_3 * doubling_factor * doubling_factor

    # L5
    removal_divisor_day_5 = 4 # one-fourth of the fish
    fish_removed_day_5 = fish_day_5_before_removal / removal_divisor_day_5

    # L6
    fish_end_day_5 = fish_day_5_before_removal - fish_removed_day_5

    # L7
    fish_day_7_before_addition = fish_end_day_5 * doubling_factor * doubling_factor

    # L8
    added_fish_day_7 = 15 # adds 15 more fish
    total_fish = fish_day_7_before_addition + added_fish_day_7

    # FA
    answer = total_fish
    return answer