def solve():
    """Index: 712.
    Returns: the amount of change Jimmy will get back.
    """
    # L1
    num_pens = 3 # 3 pens
    cost_per_pen = 1 # $1 each
    cost_pens = num_pens * cost_per_pen

    # L2
    num_notebooks = 4 # 4 notebooks
    cost_per_notebook = 3 # $3 each
    cost_notebooks = num_notebooks * cost_per_notebook

    # L3
    num_folders = 2 # 2 folders
    cost_per_folder = 5 # $5 each
    cost_folders = num_folders * cost_per_folder

    # L4
    total_spent = cost_pens + cost_notebooks + cost_folders

    # L5
    paid_amount = 50 # $50 bill
    change = paid_amount - total_spent

    # FA
    answer = change
    return answer