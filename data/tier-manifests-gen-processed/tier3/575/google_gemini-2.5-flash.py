def solve():
    """Index: 575.
    Returns: the number of calories John ate.
    """
    # L1
    servings_per_package = 3 # 3 servings
    calories_per_serving = 120 # 120 calories each
    total_calories_in_package = servings_per_package * calories_per_serving

    # L2
    portion_denominator = 2 # half the package
    calories_eaten = total_calories_in_package / portion_denominator

    # FA
    answer = calories_eaten
    return answer