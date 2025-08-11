def solve():
    """Index: 5121.
    Returns: the number of rhinestones Andrea still needs.
    """
    # L1
    total_needed = 45 # Andrea needs 45 rhinestones
    bought_divisor = 3 # a third of what she needed
    rhinestones_bought = total_needed / bought_divisor

    # L2
    found_divisor = 5 # a fifth of what she needed
    rhinestones_found = total_needed / found_divisor

    # L3
    rhinestones_still_needed = total_needed - rhinestones_bought - rhinestones_found

    # FA
    answer = rhinestones_still_needed
    return answer