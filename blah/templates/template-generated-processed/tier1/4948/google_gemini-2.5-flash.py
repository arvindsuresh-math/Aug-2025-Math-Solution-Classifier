def solve():
    """Index: 4948.
    Returns: the total number of decorations handed out.
    """
    # L1
    tinsel_per_box = 4 # 4 pieces of tinsel
    tree_per_box = 1 # 1 Christmas tree
    snow_globes_per_box = 5 # 5 snow globes
    decorations_per_box = tinsel_per_box + tree_per_box + snow_globes_per_box

    # L2
    num_family_boxes = 11 # 11 families receive a box of decorations
    num_community_boxes = 1 # another box is given to the community center
    total_boxes = num_family_boxes + num_community_boxes

    # L3
    total_decorations = decorations_per_box * total_boxes

    # FA
    answer = total_decorations
    return answer