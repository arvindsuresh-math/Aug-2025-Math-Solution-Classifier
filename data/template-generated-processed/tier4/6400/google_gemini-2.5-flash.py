def solve():
    """Index: 6400.
    Returns: the cost of each notebook.
    """
    # L1
    num_items_pens_pencils = 2 # WK
    cost_per_item_pens_pencils = 1.00 # both the pens and pencils cost $1.00 each
    cost_pens_pencils = num_items_pens_pencils * cost_per_item_pens_pencils

    # L2
    backpack_cost = 15 # backpack costs $15
    cost_backpack_pens_pencils = backpack_cost + cost_pens_pencils

    # L3
    total_spent = 32 # Dan spent $32
    remaining_spent = total_spent - cost_backpack_pens_pencils

    # L4
    num_notebooks = 5 # 5 multi-subject notebooks
    cost_per_notebook = remaining_spent / num_notebooks

    # FA
    answer = cost_per_notebook
    return answer