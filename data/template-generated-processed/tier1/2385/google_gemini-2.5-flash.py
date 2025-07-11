def solve():
    """Index: 2385.
    Returns: the total number of cans Jack can store in each closet.
    """
    # L1
    cans_per_row = 12 # 12 cans in one row
    rows_per_shelf = 4 # 4 rows on one shelf
    cans_per_shelf = cans_per_row * rows_per_shelf

    # L2
    shelves_per_closet = 10 # 10 shelves in one closet
    total_cans_in_closet = cans_per_shelf * shelves_per_closet

    # FA
    answer = total_cans_in_closet
    return answer