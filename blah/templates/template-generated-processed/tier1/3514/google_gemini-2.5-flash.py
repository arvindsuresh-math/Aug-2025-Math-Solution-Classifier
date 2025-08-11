def solve():
    """Index: 3514.
    Returns: the total number of notebooks bought for the children.
    """
    # L1
    john_notebooks_per_child = 2 # bought 2 notebooks for each of his children
    num_children = 3 # John has 3 children
    john_total_notebooks = john_notebooks_per_child * num_children

    # L2
    wife_notebooks_per_child = 5 # John's wife bought 5 notebooks for each of them
    wife_total_notebooks = wife_notebooks_per_child * num_children

    # L3
    total_notebooks = john_total_notebooks + wife_total_notebooks

    # FA
    answer = total_notebooks
    return answer