def solve():
    """Index: 4224.
    Returns: the cost of each green notebook.
    """
    # L1
    black_notebook_cost = 15 # the black notebook cost $15
    pink_notebook_cost = 10 # the pink one cost $10
    black_and_pink_cost = black_notebook_cost + pink_notebook_cost

    # L2
    total_cost = 45 # The total cost was $45
    total_green_notebooks_cost = total_cost - black_and_pink_cost

    # L3
    num_green_notebooks = 2 # 2 of them are green
    cost_per_green_notebook = total_green_notebooks_cost / num_green_notebooks

    # FA
    answer = cost_per_green_notebook
    return answer