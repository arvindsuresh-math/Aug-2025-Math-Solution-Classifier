def solve():
    """Index: 712.
    Returns: the amount of change Jimmy will get back after his purchases.
    """
    # L1
    num_pens = 3 # 3 pens for school
    price_per_pen = 1 # $1 each
    pens_total = num_pens * price_per_pen

    # L2
    num_notebooks = 4 # 4 notebooks
    price_per_notebook = 3 # $3 each
    notebooks_total = num_notebooks * price_per_notebook

    # L3
    num_folders = 2 # 2 folders
    price_per_folder = 5 # $5 each
    folders_total = num_folders * price_per_folder

    # L4
    total_spent = pens_total + notebooks_total + folders_total

    # L5
    bill_amount = 50 # paid with a $50 bill
    change = bill_amount - total_spent

    # FA
    answer = change
    return answer