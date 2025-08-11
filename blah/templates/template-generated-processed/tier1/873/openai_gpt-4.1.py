def solve():
    """Index: 873.
    Returns: the total mass of fruit harvested in the orchard.
    """
    # L1
    num_apple_trees = 30 # 30 apple trees
    apple_kg_per_tree = 150 # each give 150 kg of apples
    apple_total_kg = num_apple_trees * apple_kg_per_tree

    # L2
    num_peach_trees = 45 # 45 peach trees
    peach_kg_per_tree = 65 # each produce an average of 65 kg of fruit
    peach_total_kg = num_peach_trees * peach_kg_per_tree

    # L3
    total_kg = apple_total_kg + peach_total_kg

    # FA
    answer = total_kg
    return answer