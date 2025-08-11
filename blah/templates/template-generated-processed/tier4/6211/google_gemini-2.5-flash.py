def solve():
    """Index: 6211.
    Returns: the height of the tree in meters.
    """
    # L1
    jane_height = 1.5 # Jane is 1.5 meters tall
    jane_shadow = 0.5 # Jane of 0.5 meters
    height_to_shadow_ratio = jane_height / jane_shadow

    # L2
    tree_shadow = 10 # the tree of 10 meters
    tree_height = height_to_shadow_ratio * tree_shadow

    # FA
    answer = tree_height
    return answer