from fractions import Fraction

def solve():
    """Index: 5.
    Returns: the total number of flowers Mark has in his garden.
    """
    # L1
    purple_percentage = Fraction(80, 100) # 80% more of those in purple
    yellow_flowers = 10 # Ten of them are yellow
    additional_purple_flowers = purple_percentage * yellow_flowers

    # L2
    purple_flowers = yellow_flowers + additional_purple_flowers

    # L3
    yellow_and_purple_flowers = yellow_flowers + purple_flowers

    # L4
    green_percentage = Fraction(25, 100) # only 25% as many green flowers
    green_flowers = green_percentage * yellow_and_purple_flowers

    # L5
    total_flowers = yellow_and_purple_flowers + green_flowers

    # FA
    answer = total_flowers
    return answer