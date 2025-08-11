def solve():
    """Index: 797.
    Returns: the total cups of dog food Hannah should prepare in a day.
    """
    # L1
    first_dog_food_cups = 1.5 # The first dog eats 1.5 cups of dog food a day
    twice_factor = 2 # twice as much
    second_dog_food_cups = first_dog_food_cups * twice_factor

    # L2
    more_than_second_dog_cups = 2.5 # eats 2.5 cups more than the second dog
    third_dog_food_cups = second_dog_food_cups + more_than_second_dog_cups

    # L3
    total_food_cups = first_dog_food_cups + second_dog_food_cups + third_dog_food_cups

    # FA
    answer = total_food_cups
    return answer