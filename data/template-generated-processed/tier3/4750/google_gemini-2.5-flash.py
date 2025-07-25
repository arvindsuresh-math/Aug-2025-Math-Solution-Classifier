from fractions import Fraction

def solve():
    """Index: 4750.
    Returns: the average number of fish in all three bodies of water.
    """
    # L1
    trout_more_than_pool = 25 # 25 more trout
    boast_pool_fish = 75 # 75 fish in Boast Pool
    onum_lake_fish = trout_more_than_pool + boast_pool_fish

    # L2
    riddle_pond_fraction = Fraction(1, 2) # half as many fish
    riddle_pond_fish = riddle_pond_fraction * onum_lake_fish

    # L3
    total_fish_three_bodies = onum_lake_fish + riddle_pond_fish + boast_pool_fish

    # L4
    number_of_bodies = 3 # all three bodies of water
    average_fish = total_fish_three_bodies / number_of_bodies

    # FA
    answer = average_fish
    return answer