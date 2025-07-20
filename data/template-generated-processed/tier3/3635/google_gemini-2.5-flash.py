def solve():
    """Index: 3635.
    Returns: the cost of each blue notebook.
    """
    # L1
    total_notebooks = 12 # a total of 12 notebooks
    red_notebooks_count = 3 # 3 red notebooks
    green_notebooks_count = 2 # 2 green notebooks
    blue_notebooks_count = total_notebooks - red_notebooks_count - green_notebooks_count

    # L2
    red_notebook_price = 4 # 4 dollars each
    cost_red_notebooks = red_notebooks_count * red_notebook_price

    # L3
    green_notebook_price = 2 # 2 dollars each
    cost_green_notebooks = green_notebooks_count * green_notebook_price

    # L4
    total_spent = 37 # spent 37 dollars on notebooks
    cost_blue_notebooks = total_spent - cost_red_notebooks - cost_green_notebooks

    # L5
    cost_per_blue_notebook = cost_blue_notebooks / blue_notebooks_count

    # FA
    answer = cost_per_blue_notebook
    return answer