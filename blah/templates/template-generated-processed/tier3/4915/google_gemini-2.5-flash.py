def solve():
    """Index: 4915.
    Returns: the grams of fat added to each serving of food.
    """
    # L1
    fat_per_cup = 88 # Cream has 88 grams of fat per cup
    cream_cup_divisor = 2 # a half cup of cream
    total_fat_added = fat_per_cup / cream_cup_divisor

    # L2
    number_of_servings = 4 # serves four people
    fat_per_serving = total_fat_added / number_of_servings

    # FA
    answer = fat_per_serving
    return answer