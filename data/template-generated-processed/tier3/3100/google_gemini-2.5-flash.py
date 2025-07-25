from fractions import Fraction

def solve():
    """Index: 3100.
    Returns: the total number of fruits eaten by the three dogs.
    """
    # L1
    blueberry_fraction = Fraction(3, 4) # 3/4 times as many blueberries
    bonnies_eaten_by_third_dog = 60 # If the dog that likes bonnies ate 60 of them
    blueberries_eaten_by_second_dog = blueberry_fraction * bonnies_eaten_by_third_dog

    # L2
    fruits_bonnies_blueberries_dogs = blueberries_eaten_by_second_dog + bonnies_eaten_by_third_dog

    # L3
    apple_multiplier = 3 # eats 3 times as many apples
    apples_eaten_by_first_dog = apple_multiplier * blueberries_eaten_by_second_dog

    # L4
    total_fruits_eaten = fruits_bonnies_blueberries_dogs + apples_eaten_by_first_dog

    # FA
    answer = total_fruits_eaten
    return answer