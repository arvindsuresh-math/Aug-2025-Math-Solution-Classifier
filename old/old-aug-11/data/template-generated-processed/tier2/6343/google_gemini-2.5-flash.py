def solve():
    """Index: 6343.
    Returns: the total amount Lyle will pay for 4 notebooks.
    """
    # L1
    pen_cost = 1.50 # a pen costs $1.50
    notebook_cost_multiplier = 3 # three times as much
    notebook_cost = pen_cost * notebook_cost_multiplier

    # L2
    num_notebooks = 4 # 4 notebooks
    total_cost = notebook_cost * num_notebooks

    # FA
    answer = total_cost
    return answer