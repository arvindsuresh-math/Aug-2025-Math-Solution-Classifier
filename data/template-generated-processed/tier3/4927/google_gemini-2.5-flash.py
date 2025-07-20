from fractions import Fraction

def solve():
    """Index: 4927.
    Returns: the average height of the trees Jackie climbed.
    """
    # L1
    first_tree_height = 1000 # a 1000 foot tall tree
    half_fraction = Fraction(1, 2) # half as tall
    height_of_second_type_tree = half_fraction * first_tree_height

    # L2
    additional_height = 200 # 200 feet taller than her first tree
    final_tree_height = first_tree_height + additional_height

    # L3
    num_trees = 4 # the 4 trees Jackie climbed
    total_height = first_tree_height + height_of_second_type_tree + height_of_second_type_tree + final_tree_height

    # L4
    average_height = total_height / num_trees

    # FA
    answer = average_height
    return answer