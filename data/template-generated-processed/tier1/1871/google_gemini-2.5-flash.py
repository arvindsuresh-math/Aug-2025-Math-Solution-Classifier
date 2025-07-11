def solve():
    """Index: 1871.
    Returns: the total number of notebooks and pens.
    """
    # L1
    more_pens_than_notebooks = 50 # 50 more pens than notebooks
    num_notebooks = 30 # 30 notebooks on the shelf
    num_pens = num_notebooks + more_pens_than_notebooks

    # L2
    total_items = num_pens + num_notebooks

    # FA
    answer = total_items
    return answer