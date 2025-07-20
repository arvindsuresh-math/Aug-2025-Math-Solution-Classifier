def solve():
    """Index: 5857.
    Returns: the total amount of food Ella and her dog eat in 10 days.
    """
    # L1
    dog_food_multiplier = 4 # 4 pounds of food for every one pound of food that Ella eats
    ella_food_per_day = 20 # Ella eat 20 pounds of food each day
    dog_food_per_day = dog_food_multiplier * ella_food_per_day

    # L2
    total_food_per_day = dog_food_per_day + ella_food_per_day

    # L3
    num_days = 10 # in 10 days
    total_food_in_10_days = num_days * total_food_per_day

    # FA
    answer = total_food_in_10_days
    return answer