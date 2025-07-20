def solve():
    """Index: 4465.
    Returns: the total number of birds eggs June found.
    """
    # L1
    num_nests_tree1 = 2 # 2 birds nest
    eggs_per_nest_tree1 = 5 # 5 eggs each
    eggs_tree1 = num_nests_tree1 * eggs_per_nest_tree1

    # L2
    eggs_nest_tree2 = 3 # 1 nest with 3 eggs in another tree
    eggs_nest_front_yard = 4 # a nest with 4 eggs in her front yard
    total_eggs = eggs_tree1 + eggs_nest_tree2 + eggs_nest_front_yard

    # FA
    answer = total_eggs
    return answer