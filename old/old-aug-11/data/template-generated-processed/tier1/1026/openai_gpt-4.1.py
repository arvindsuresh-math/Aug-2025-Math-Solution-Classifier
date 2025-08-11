def solve():
    """Index: 1026.
    Returns: the combined height of Mr. Martinez and Chiquita in feet.
    """
    # L1
    chiquita_height = 5 # Chiquita is 5 feet tall
    martinez_taller_by = 2 # two feet taller than his daughter
    martinez_height = chiquita_height + martinez_taller_by

    # L2
    combined_height = martinez_height + chiquita_height

    # FA
    answer = combined_height
    return answer