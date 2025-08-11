def solve():
    """Index: 3328.
    Returns: the amount of food the third dog eats a week.
    """
    # L1
    first_dog_food = 13 # One dog eats 13 pounds a week
    double_factor = 2 # The second eats double this
    second_dog_food = first_dog_food * double_factor

    # L2
    num_dogs = 3 # Arthur has 3 dogs
    average_food_per_dog_per_week = 15 # an average of 15 pounds of food a week
    total_food_all_dogs = num_dogs * average_food_per_dog_per_week

    # L3
    third_dog_food = total_food_all_dogs - first_dog_food - second_dog_food

    # FA
    answer = third_dog_food
    return answer