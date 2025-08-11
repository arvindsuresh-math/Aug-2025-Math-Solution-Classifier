from fractions import Fraction

def solve():
    """Index: 7399.
    Returns: the total number of pieces of fruit in the fruit basket.
    """
    # L1
    oranges = 6 # six oranges
    apples_fewer = 2 # two fewer apples
    apples = oranges - apples_fewer

    # L2
    bananas_multiplier = 3 # 3 times as many bananas
    bananas = bananas_multiplier * apples

    # L3
    peaches_fraction = Fraction(1, 2) # half as many peaches
    peaches = peaches_fraction * bananas

    # L4
    total_fruit = oranges + apples + bananas + peaches

    # FA
    answer = total_fruit
    return answer