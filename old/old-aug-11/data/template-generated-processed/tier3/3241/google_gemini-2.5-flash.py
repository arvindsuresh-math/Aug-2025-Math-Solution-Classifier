from fractions import Fraction

def solve():
    """Index: 3241.
    Returns: the number of sushi rolls James made.
    """
    # L1
    total_fish_bought = 400 # buys 400 fish
    bad_percentage = Fraction(20, 100) # 20% of the fish have gone bad
    bad_fish = bad_percentage * total_fish_bought

    # L2
    remaining_fish = total_fish_bought - bad_fish

    # L3
    fish_per_sushi_roll = 40 # 40 fish to make one sushi roll
    sushi_rolls_made = remaining_fish / fish_per_sushi_roll

    # FA
    answer = sushi_rolls_made
    return answer