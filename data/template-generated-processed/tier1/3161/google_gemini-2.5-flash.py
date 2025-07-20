def solve():
    """Index: 3161.
    Returns: the number of eggs Trevor had left.
    """
    # L1
    gertrude_eggs = 4 # 4 eggs from Gertrude
    blanche_eggs = 3 # 3 eggs from Blanche
    nancy_eggs = 2 # Nancy laid 2 eggs
    martha_eggs = 2 # as did Martha
    total_collected_eggs = gertrude_eggs + blanche_eggs + nancy_eggs + martha_eggs

    # L2
    dropped_eggs = 2 # dropped 2 eggs
    eggs_left = total_collected_eggs - dropped_eggs

    # FA
    answer = eggs_left
    return answer