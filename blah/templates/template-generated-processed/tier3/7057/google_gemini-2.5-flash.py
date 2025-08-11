from fractions import Fraction

def solve():
    """Index: 7057.
    Returns: the number of yellow flowers in the garden.
    """
    # L1
    red_multiplier = 3 # three times more red flowers
    green_flowers = 9 # 9 green flowers
    red_flowers = red_multiplier * green_flowers

    # L2
    blue_percentage = Fraction(50, 100) # Blue flowers make up to 50% of the total flower count
    total_flowers = 96 # In total there are 96 flowers
    blue_flowers = blue_percentage * total_flowers

    # L3
    yellow_flowers = total_flowers - blue_flowers - red_flowers - green_flowers

    # FA
    answer = yellow_flowers
    return answer