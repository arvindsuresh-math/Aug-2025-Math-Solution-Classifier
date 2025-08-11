def solve():
    """Index: 2077.
    Returns: the total amount Liz spent in dollars.
    """
    # L1
    recipe_book_cost = 6 # recipe book that cost $6
    multiplier_for_baking_dish = 2 # twice as much
    baking_dish_cost = recipe_book_cost * multiplier_for_baking_dish

    # L2
    num_ingredients = 5 # five ingredients
    cost_per_ingredient = 3 # $3 each
    ingredients_total_cost = num_ingredients * cost_per_ingredient

    # L3
    apron_extra_cost = 1 # a dollar more than the recipe book
    apron_cost = recipe_book_cost + apron_extra_cost

    # L4
    total_spent = recipe_book_cost + baking_dish_cost + ingredients_total_cost + apron_cost

    # FA
    answer = total_spent
    return answer