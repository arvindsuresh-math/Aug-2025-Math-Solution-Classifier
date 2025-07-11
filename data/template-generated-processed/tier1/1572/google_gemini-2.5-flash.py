def solve():
    """Index: 1572.
    Returns: the total number of sheets of paper Barbara removed from the chest of drawers.
    """
    # L1
    num_bundles_colored_paper = 3 # 3 bundles of colored paper
    sheets_per_bundle = 2 # a bundle holds 2 sheets of paper
    sheets_colored_paper = num_bundles_colored_paper * sheets_per_bundle

    # L2
    num_bunches_white_paper = 2 # 2 bunches of white paper
    sheets_per_bunch = 4 # a bunch holds 4 sheets of paper
    sheets_white_paper = num_bunches_white_paper * sheets_per_bunch

    # L3
    num_heaps_scrap_paper = 5 # 5 heaps of scrap paper
    sheets_per_heap = 20 # a heap holds 20 sheets of paper
    sheets_scrap_paper = num_heaps_scrap_paper * sheets_per_heap

    # L4
    total_sheets_removed = sheets_colored_paper + sheets_white_paper + sheets_scrap_paper

    # FA
    answer = total_sheets_removed
    return answer