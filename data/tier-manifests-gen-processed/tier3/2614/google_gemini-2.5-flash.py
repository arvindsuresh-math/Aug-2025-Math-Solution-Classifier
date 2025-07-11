def solve():
    """Index: 2614.
    Returns: the number of eggs Megan would have per meal.
    """
    # L1
    dozen_eggs = 12 # a dozen eggs
    total_eggs_initial = dozen_eggs + dozen_eggs

    # L2
    omelet_eggs = 2 # 2 eggs to make an omelet
    cake_eggs = 4 # 4 eggs to bake a cake
    eggs_after_baking = total_eggs_initial - omelet_eggs - cake_eggs

    # L3
    aunt_share_divisor = 2 # half of her remaining eggs
    eggs_after_aunt_share = eggs_after_baking / aunt_share_divisor

    # L4
    num_meals = 3 # next 3 meals
    eggs_per_meal = eggs_after_aunt_share / num_meals

    # FA
    answer = eggs_per_meal
    return answer