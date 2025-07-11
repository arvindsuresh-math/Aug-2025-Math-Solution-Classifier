from fractions import Fraction

def solve():
    """Index: 1786.
    Returns: the percentage chance of getting 5 pieces of candy.
    """
    # L1
    blue_egg_fraction = Fraction(4, 5) # 4/5 of the Easter eggs are blue
    blue_egg_five_candy_multiplier = Fraction(1, 4) # 1/4 of the blue eggs do
    prob_blue_five_candy_fraction = blue_egg_fraction * blue_egg_five_candy_multiplier
    prob_blue_five_candy_percentage = prob_blue_five_candy_fraction * 100

    # L2
    purple_egg_fraction = Fraction(1, 5) # 1/5 are purple
    purple_egg_five_candy_multiplier = Fraction(1, 2) # Half the purple eggs have five pieces of candy
    prob_purple_five_candy_fraction = purple_egg_fraction * purple_egg_five_candy_multiplier
    prob_purple_five_candy_percentage = prob_purple_five_candy_fraction * 100

    # L3
    total_five_candy_percentage = prob_blue_five_candy_percentage + prob_purple_five_candy_percentage

    # FA
    answer = total_five_candy_percentage
    return answer