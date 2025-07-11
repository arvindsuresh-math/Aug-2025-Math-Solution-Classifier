def solve():
    """Index: 1871.
    Returns: the total number of notebooks and pens on the shelf.
    """
    # L1
    notebooks = 30 # 30 notebooks on the shelf
    pens_more_than_notebooks = 50 # 50 more pens than notebooks
    pens = pens_more_than_notebooks + notebooks

    # L2
    total_items = pens + notebooks

    # FA
    answer = total_items
    return answer