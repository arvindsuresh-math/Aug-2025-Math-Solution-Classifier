def solve():
    """Index: 1136.
    Returns: the total kilograms of food needed.
    """
    # L1
    num_dogs = 4 # 4 dogs
    food_per_dog_grams = 250 # 250 grams of food per day
    daily_food_total_grams = num_dogs * food_per_dog_grams

    # L3
    vacation_days = 14 # 14 days
    grams_per_kilogram = 1000 # WK
    daily_food_total_kg = daily_food_total_grams / grams_per_kilogram
    total_food_kg = vacation_days * daily_food_total_kg

    # FA
    answer = total_food_kg
    return answer