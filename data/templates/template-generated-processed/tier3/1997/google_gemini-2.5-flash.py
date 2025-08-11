from fractions import Fraction

def solve():
    """Index: 1997.
    Returns: the difference in pounds of food eaten per day between Elmer the elephant and Penelope the pig.
    """
    # L1
    penelope_food_per_day = 20 # Penelope the pig eats 20 pounds of food per day
    penelope_greta_ratio = 10 # 10 times more than Greta the goose eats
    greta_food_per_day = penelope_food_per_day / penelope_greta_ratio

    # L2
    milton_greta_fraction = Fraction(1, 100) # 1/100 as much as Greta the goose eats per day
    milton_food_per_day = milton_greta_fraction * greta_food_per_day

    # L3
    elmer_milton_multiplier = 4000 # 4000 times more than Milton the mouse does per day
    elmer_food_per_day = elmer_milton_multiplier * milton_food_per_day

    # L4
    difference_elmer_penelope = elmer_food_per_day - penelope_food_per_day

    # FA
    answer = difference_elmer_penelope
    return answer