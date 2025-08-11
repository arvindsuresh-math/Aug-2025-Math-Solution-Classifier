from fractions import Fraction

def solve():
    """Index: 3337.
    Returns: the total number of white-spotted mushrooms gathered.
    """
    # L1
    red_mushrooms = 12 # 12 red mushrooms
    red_spotted_fraction = Fraction(2, 3) # two-thirds of the red mushrooms
    spotted_red_mushrooms = red_spotted_fraction * red_mushrooms

    # L2
    brown_mushrooms = 6 # 6 brown mushrooms
    brown_spotted_percentage = Fraction(100, 100) # all of the brown mushrooms
    spotted_brown_mushrooms = brown_spotted_percentage * brown_mushrooms

    # L3
    green_mushrooms = 14 # 14 green mushrooms
    green_spotted_percentage = 0 # 0%
    spotted_green_mushrooms = green_mushrooms * green_spotted_percentage

    # L4
    blue_mushrooms = 6 # 6 blue mushrooms
    blue_spotted_fraction = Fraction(1, 2) # half of the blue mushrooms
    spotted_blue_mushrooms = blue_spotted_fraction * blue_mushrooms

    # L5
    total_spotted_mushrooms = spotted_red_mushrooms + spotted_brown_mushrooms + spotted_green_mushrooms + spotted_blue_mushrooms

    # FA
    answer = total_spotted_mushrooms
    return answer