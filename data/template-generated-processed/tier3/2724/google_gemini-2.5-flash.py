def solve():
    """Index: 2724.
    Returns: the total number of servings of vegetables Jimmy is growing.
    """
    # L1
    carrot_servings_per_plant = 4 # each carrot produces 4 servings of vegetables
    corn_multiplier = 5 # 5 times as many servings of veggies
    corn_servings_per_plant = carrot_servings_per_plant * corn_multiplier

    # L2
    green_bean_divisor = 2 # half as many servings
    green_bean_servings_per_plant = corn_servings_per_plant / green_bean_divisor

    # L3
    plants_per_plot = 9 # each plot has 9 plants
    total_carrot_servings = carrot_servings_per_plant * plants_per_plot

    # L4
    total_corn_servings = corn_servings_per_plant * plants_per_plot

    # L5
    total_green_bean_servings = green_bean_servings_per_plant * plants_per_plot

    # L6
    total_servings = total_carrot_servings + total_corn_servings + total_green_bean_servings

    # FA
    answer = total_servings
    return answer