def solve():
    """Index: 6581.
    Returns: the profit Andy makes for each cake.
    """
    # L1
    total_ingredient_cost = 12 # $12 on ingredients
    num_cakes_for_ingredients = 2 # two cakes
    ingredient_cost_per_cake = total_ingredient_cost / num_cakes_for_ingredients

    # L2
    packaging_cost_per_cake = 1 # $1 on packaging for each cake
    total_cost_per_cake = ingredient_cost_per_cake + packaging_cost_per_cake

    # L3
    selling_price_per_cake = 15 # sells each cake for $15
    profit_per_cake = selling_price_per_cake - total_cost_per_cake

    # FA
    answer = profit_per_cake
    return answer