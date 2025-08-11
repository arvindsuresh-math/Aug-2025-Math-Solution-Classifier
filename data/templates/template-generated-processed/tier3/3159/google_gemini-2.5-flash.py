from fractions import Fraction

def solve():
    """Index: 3159.
    Returns: the total amount of food Layla has to give to her fish.
    """
    # L1
    num_goldfish = 2 # two Goldfish
    goldfish_food_per_fish = 1 # one teaspoon of fish food
    total_goldfish_food = num_goldfish * goldfish_food_per_fish

    # L2
    num_swordtails = 3 # 3 Swordtails
    swordtail_food_per_fish = 2 # 2 teaspoons of food
    total_swordtail_food = num_swordtails * swordtail_food_per_fish

    # L3
    num_guppies = 8 # 8 Guppies
    guppy_food_per_fish = Fraction(1, 2) # half a teaspoon of food
    total_guppy_food = num_guppies * guppy_food_per_fish

    # L4
    total_food = total_goldfish_food + total_swordtail_food + total_guppy_food

    # FA
    answer = total_food
    return answer