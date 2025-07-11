def solve():
    """Index: 1572.
    Returns: the total number of sheets of paper Barbara removed from the chest of drawers.
    """
    # L1
    num_bundles_colored = 3 # 3 bundles of colored paper
    sheets_per_bundle = 2 # a bundle holds 2 sheets of paper
    colored_sheets = num_bundles_colored * sheets_per_bundle

    # L2
    num_bunches_white = 2 # 2 bunches of white paper
    sheets_per_bunch = 4 # a bunch holds 4 sheets of paper
    white_sheets = num_bunches_white * sheets_per_bunch

    # L3
    num_heaps_scrap = 5 # 5 heaps of scrap paper
    sheets_per_heap = 20 # a heap holds 20 sheets of paper
    scrap_sheets = num_heaps_scrap * sheets_per_heap

    # L4
    total_sheets = colored_sheets + white_sheets + scrap_sheets

    # FA
    answer = total_sheets
    return answer