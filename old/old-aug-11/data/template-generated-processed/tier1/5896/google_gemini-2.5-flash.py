def solve():
    """Index: 5896.
    Returns: the total number of parents in the auditorium.
    """
    # L1
    num_girls = 6 # 6 girls
    num_boys = 8 # 8 boys
    total_kids = num_girls + num_boys

    # L2
    parents_per_kid = 2 # both parents of each kid
    total_parents = total_kids * parents_per_kid

    # FA
    answer = total_parents
    return answer