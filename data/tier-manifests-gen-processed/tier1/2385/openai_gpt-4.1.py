def solve():
    """Index: 2385.
    Returns: the number of cans Jack can store in each closet.
    """
    # L1
    cans_per_row = 12 # 12 cans in one row
    rows_per_shelf = 4 # 4 rows on one shelf
    cans_per_shelf = cans_per_row * rows_per_shelf

    # L2
    shelves_per_closet = 10 # 10 shelves in one closet
    cans_per_closet = cans_per_shelf * shelves_per_closet

    # FA
    answer = cans_per_closet
    return answer