def solve():
    """Index: 5130.
    Returns: the amount of dog food Paul needs each day.
    """
    # L1
    dog_weight_1 = 20 # One weighs 20 pounds
    dog_weight_2 = 40 # One weighs 40
    dog_weight_3 = 10 # Another weighs 10
    dog_weight_4 = 30 # One weighs 30
    dog_weight_5 = 50 # and the final one weighs 50 pounds
    total_dog_weight = dog_weight_1 + dog_weight_2 + dog_weight_3 + dog_weight_4 + dog_weight_5

    # L2
    weight_per_pound_food = 10 # For every 10 pounds they weigh, they need 1 pound of dog food per day
    daily_food_needed = total_dog_weight / weight_per_pound_food

    # FA
    answer = daily_food_needed
    return answer