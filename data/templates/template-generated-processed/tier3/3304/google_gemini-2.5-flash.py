from fractions import Fraction

def solve():
    """Index: 3304.
    Returns: the total number of fruits Emiliano consumed.
    """
    # L1
    apples = 15 # 15 apples
    apple_orange_ratio = 4 # four times as many apples as oranges
    oranges = apples * apple_orange_ratio

    # L2
    eaten_fraction = Fraction(2, 3) # 2/3 of each fruit's quantity
    eaten_oranges = eaten_fraction * oranges

    # L3
    eaten_apples = eaten_fraction * apples

    # L4
    total_fruits_eaten = eaten_apples + eaten_oranges

    # FA
    answer = total_fruits_eaten
    return answer