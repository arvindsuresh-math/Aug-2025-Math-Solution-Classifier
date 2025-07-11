def solve():
    """Index: 1679.
    Returns: the total number of trees in the park.
    """
    # L1
    park_length = 1000 # 1000 feet long
    park_width = 2000 # 2000 feet wide
    park_area = park_length * park_width

    # L2
    trees_per_square_feet = 20 # 1 tree per 20 square feet
    total_trees = park_area / trees_per_square_feet

    # FA
    answer = total_trees
    return answer