def solve():
    """Index: 575.
    Returns: the number of calories John ate.
    """
    # L1
    servings_per_package = 3 # 3 servings
    calories_per_serving = 120 # 120 calories each
    total_calories = servings_per_package * calories_per_serving

    # L2
    half_package = 2 # eats half the package
    calories_eaten = total_calories / half_package

    # FA
    answer = calories_eaten
    return answer