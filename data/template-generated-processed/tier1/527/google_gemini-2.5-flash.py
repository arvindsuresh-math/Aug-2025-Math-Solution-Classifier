def solve():
    """Index: 527.
    Returns: the total number of calories in the salad.
    """
    # L1
    crouton_calories_per_crouton = 20 # 20 calories each
    num_croutons = 12 # 12 croutons
    total_crouton_calories = crouton_calories_per_crouton * num_croutons

    # L2
    lettuce_calories = 30 # 30 calories
    cucumber_calories = 80 # 80 calories
    total_salad_calories = total_crouton_calories + lettuce_calories + cucumber_calories

    # FA
    answer = total_salad_calories
    return answer