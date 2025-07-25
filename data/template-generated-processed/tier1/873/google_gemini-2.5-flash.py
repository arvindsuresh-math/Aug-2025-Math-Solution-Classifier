def solve():
    """Index: 873.
    Returns: the total mass of fruit harvested in the orchard.
    """
    # L1
    num_apple_trees = 30 # 30 apple trees
    kg_per_apple_tree = 150 # 150 kg of apples
    total_apple_kg = num_apple_trees * kg_per_apple_tree

    # L2
    num_peach_trees = 45 # 45 peach trees
    kg_per_peach_tree = 65 # 65 kg of fruit
    total_peach_kg = num_peach_trees * kg_per_peach_tree

    # L3
    total_fruit_mass = total_apple_kg + total_peach_kg

    # FA
    answer = total_fruit_mass
    return answer