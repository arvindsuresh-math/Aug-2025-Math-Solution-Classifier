def solve():
    """Index: 6645.
    Returns: the total number of children Sandro has.
    """
    # L1
    num_sons = 3 # three sons
    daughters_multiplier = 6 # six times as many daughters as sons
    num_daughters = num_sons * daughters_multiplier

    # L2
    total_children = num_daughters + num_sons

    # FA
    answer = total_children
    return answer