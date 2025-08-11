from fractions import Fraction

def solve():
    """Index: 3759.
    Returns: the total number of bottles the first house received.
    """
    # L1
    only_cider_bottles = 40 # 40 contain only cider
    only_beer_bottles = 80 # 80 contain only beer
    cider_and_beer_bottles = only_cider_bottles + only_beer_bottles

    # L2
    total_bottles = 180 # 180 bottles of drinks
    mixture_bottles = total_bottles - cider_and_beer_bottles

    # L3
    delivery_fraction = Fraction(1, 2) # half the number of each bottle
    first_house_cider = delivery_fraction * only_cider_bottles

    # L4
    first_house_beer = delivery_fraction * only_beer_bottles

    # L5
    first_house_cider_beer_total = first_house_beer + first_house_cider

    # L6
    first_house_mixture = delivery_fraction * mixture_bottles

    # L7
    total_bottles_first_house = first_house_cider_beer_total + first_house_mixture

    # FA
    answer = total_bottles_first_house
    return answer