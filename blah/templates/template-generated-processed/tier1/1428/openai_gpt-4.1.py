def solve():
    """Index: 1428.
    Returns: the total number of figurines Adam can make from all his wood blocks.
    """
    # L1
    basswood_blocks = 15 # 15 blocks of basswood
    figurines_per_basswood = 3 # a block of basswood can create 3 figurines
    basswood_figurines = basswood_blocks * figurines_per_basswood

    # L2
    aspen_multiplier = 2 # Aspen wood can make twice the amount of figurines compared to basswood
    figurines_per_aspen = figurines_per_basswood * aspen_multiplier

    # L3
    aspen_blocks = 20 # 20 blocks of Aspen wood
    aspen_figurines = aspen_blocks * figurines_per_aspen

    # L4
    butternut_blocks = 20 # 20 blocks of butternut wood
    figurines_per_butternut = 4 # a block of butternut wood can create 4 figurines
    butternut_figurines = butternut_blocks * figurines_per_butternut

    # L5
    total_figurines = aspen_figurines + butternut_figurines + basswood_figurines

    # FA
    answer = total_figurines
    return answer