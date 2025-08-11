def solve():
    """Index: 1384.
    Returns: the number of shelves Bill needs to stock all the pots.
    """
    # L1
    pots_per_vertical_stack = 5 # five pots vertically
    sets_side_by_side = 3 # three sets of vertically stacked pots side-by-side
    pots_per_shelf = pots_per_vertical_stack * sets_side_by_side

    # L2
    total_pots = 60 # stack 60 pots
    shelves_needed = total_pots / pots_per_shelf

    # FA
    answer = shelves_needed
    return answer