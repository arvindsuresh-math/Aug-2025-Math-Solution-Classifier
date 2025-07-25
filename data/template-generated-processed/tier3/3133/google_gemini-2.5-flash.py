def solve():
    """Index: 3133.
    Returns: the total money the sisters will make from selling orange juice.
    """
    # L1
    gabriela_oranges_per_tree = 600 # Gabriela's grove produced 600 oranges per tree
    num_trees_per_grove = 110 # 110 trees
    gabriela_total_oranges = gabriela_oranges_per_tree * num_trees_per_grove

    # L2
    alba_oranges_per_tree = 400 # Alba harvested 400 per tree
    alba_total_oranges = alba_oranges_per_tree * num_trees_per_grove

    # L3
    maricela_oranges_per_tree = 500 # Each of Maricela's trees produced 500 oranges
    maricela_total_oranges = maricela_oranges_per_tree * num_trees_per_grove

    # L4
    total_oranges_harvested = gabriela_total_oranges + alba_total_oranges + maricela_total_oranges

    # L5
    oranges_per_cup = 3 # it takes three medium-sized oranges to make 1 cup of juice
    total_cups_of_juice = total_oranges_harvested / oranges_per_cup

    # L6
    price_per_cup = 4 # they sell each cup for $4
    total_sales = total_cups_of_juice * price_per_cup

    # FA
    answer = total_sales
    return answer