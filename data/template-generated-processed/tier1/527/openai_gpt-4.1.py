def solve():
    """Index: 527.
    Returns: the total number of calories in the salad.
    """
    # L1
    croutons_count = 12 # 12 croutons
    calories_per_crouton = 20 # 20 calories each
    croutons_total_calories = calories_per_crouton * croutons_count

    # L2
    lettuce_calories = 30 # lettuce has 30 calories
    cucumber_calories = 80 # cucumber has 80 calories
    total_calories = croutons_total_calories + lettuce_calories + cucumber_calories

    # FA
    answer = total_calories
    return answer