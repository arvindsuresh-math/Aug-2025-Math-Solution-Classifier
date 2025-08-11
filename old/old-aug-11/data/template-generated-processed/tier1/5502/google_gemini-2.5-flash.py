def solve():
    """Index: 5502.
    Returns: the total number of novels and writing books Edith has.
    """
    # L1
    novels_on_shelf = 80 # 80 novels stuffed on her schoolbook shelf
    multiplier_for_twice = 2 # half as many as implies twice
    writing_books = novels_on_shelf * multiplier_for_twice

    # L2
    total_books = writing_books + novels_on_shelf

    # FA
    answer = total_books
    return answer