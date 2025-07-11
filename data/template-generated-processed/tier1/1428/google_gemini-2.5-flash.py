def solve():
    """Index: 1428.
    Returns: the total number of figurines Adam can make.
    """
    # L1
    basswood_blocks_owned = 15 # 15 blocks of basswood
    basswood_figurines_per_block = 3 # a block of basswood can create 3 figurines
    total_basswood_figurines = basswood_blocks_owned * basswood_figurines_per_block

    # L2
    aspen_multiplier_basswood = 2 # twice the amount of figurines compared to basswood
    aspen_figurines_per_block = basswood_figurines_per_block * aspen_multiplier_basswood

    # L3
    aspen_blocks_owned = 20 # 20 blocks of Aspen wood
    total_aspen_figurines = aspen_blocks_owned * aspen_figurines_per_block

    # L4
    butternut_blocks_owned = 20 # 20 blocks of butternut wood
    butternut_figurines_per_block = 4 # a block of butternut wood can create 4 figurines
    total_butternut_figurines = butternut_blocks_owned * butternut_figurines_per_block

    # L5
    total_figurines = total_aspen_figurines + total_butternut_figurines + total_basswood_figurines

    # FA
    answer = total_figurines
    return answer