def solve():
    """Index: 3854.
    Returns: the number of notebooks Sara's sister has now.
    """
    # L1
    initial_notebooks = 4 # 4 small notebooks
    ordered_notebooks = 6 # ordered 6 more notebooks
    total_after_order = initial_notebooks + ordered_notebooks

    # L2
    lost_notebooks = 2 # lost 2
    remaining_notebooks = total_after_order - lost_notebooks

    # FA
    answer = remaining_notebooks
    return answer