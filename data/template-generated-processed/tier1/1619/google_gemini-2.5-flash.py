def solve():
    """Index: 1619.
    Returns: the total number of blocks of wood Ragnar gets after 5 days.
    """
    # L1
    blocks_per_tree = 3 # 3 blocks of wood for every tree
    trees_per_day = 2 # chops 2 trees every day
    blocks_per_day = blocks_per_tree * trees_per_day

    # L2
    num_days = 5 # after 5 days
    total_blocks = blocks_per_day * num_days

    # FA
    answer = total_blocks
    return answer