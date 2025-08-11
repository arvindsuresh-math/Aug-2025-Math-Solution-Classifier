def solve():
    """Index: 4756.
    Returns: the total cost to plant the trees.
    """
    # L1
    initial_temperature = 80 # from 80
    final_temperature = 78.2 # to 78.2
    temperature_drop = initial_temperature - final_temperature

    # L2
    temp_drop_per_tree = 0.1 # drops .1 degree
    num_trees_planted = temperature_drop / temp_drop_per_tree

    # L3
    cost_per_tree = 6 # A tree costs $6 to plant
    total_cost = num_trees_planted * cost_per_tree

    # FA
    answer = total_cost
    return answer