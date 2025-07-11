def solve():
    """Index: 1136.
    Returns: the number of kilograms of food Emily should buy for her 4 dogs for 14 days.
    """
    # L1
    num_dogs = 4 # 4 dogs in her home
    food_per_dog_per_day_grams = 250 # Each one eats 250 grams of food per day
    total_food_per_day_grams = num_dogs * food_per_dog_per_day_grams

    # L2
    grams_per_kilogram = 1000 # 1.000 grams is equal a 1 kilogram
    total_food_per_day_kg = total_food_per_day_grams / grams_per_kilogram

    # L3
    vacation_days = 14 # vacation for 14 days
    total_food_needed_kg = vacation_days * total_food_per_day_kg

    # FA
    answer = total_food_needed_kg
    return answer