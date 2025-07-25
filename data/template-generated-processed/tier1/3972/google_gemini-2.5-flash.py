def solve():
    """Index: 3972.
    Returns: the total number of calories Zoe ate.
    """
    # L1
    num_strawberries = 12 # 12 strawberries
    calories_per_strawberry = 4 # 4 calories each
    calories_from_strawberries = num_strawberries * calories_per_strawberry

    # L2
    ounces_yogurt = 6 # 6 ounces of yogurt
    calories_per_ounce_yogurt = 17 # 17 calories per ounce
    calories_from_yogurt = ounces_yogurt * calories_per_ounce_yogurt

    # L3
    total_calories = calories_from_strawberries + calories_from_yogurt

    # FA
    answer = total_calories
    return answer