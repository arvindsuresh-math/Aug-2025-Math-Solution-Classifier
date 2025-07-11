def solve():
    """Index: 868.
    Returns: the distance from the base where the flagpole broke.
    """
    # L1
    total_height = 12 # A flagpole is 12 feet tall
    dangling_height = 2 # dangling two feet above the ground
    division_factor = 2 # folding over in half
    break_from_top = (total_height - dangling_height) / division_factor

    # L2
    break_from_base = total_height - break_from_top

    # FA
    answer = break_from_base
    return answer