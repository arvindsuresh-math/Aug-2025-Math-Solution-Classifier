def solve():
    """Index: 2077.
    Returns: the total amount in dollars Liz spent.
    """
    # L1
    recipe_book_cost = 6 # recipe book that cost $6
    baking_dish_multiplier = 2 # baking dish that cost twice as much
    baking_dish_cost = recipe_book_cost * baking_dish_multiplier

    # L2
    num_ingredients = 5 # five ingredients
    ingredient_cost = 3 # cost $3 each
    ingredients_total_cost = num_ingredients * ingredient_cost

    # L3
    apron_extra = 1 # apron that cost a dollar more than the recipe book
    apron_cost = recipe_book_cost + apron_extra

    # L4
    total_spent = recipe_book_cost + baking_dish_cost + ingredients_total_cost + apron_cost

    # FA
    answer = total_spent
    return answer