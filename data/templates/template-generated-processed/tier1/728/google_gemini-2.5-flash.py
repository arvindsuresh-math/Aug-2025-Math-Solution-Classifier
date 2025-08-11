def solve():
    """Index: 728.
    Returns: the amount of money Whitney will have left over after the purchase.
    """
    # L1
    num_posters = 2 # 2 posters
    cost_per_poster = 5 # $5
    total_cost_posters = num_posters * cost_per_poster

    # L2
    num_notebooks = 3 # 3 notebooks
    cost_per_notebook = 4 # $4
    total_cost_notebooks = num_notebooks * cost_per_notebook

    # L3
    num_bookmarks = 2 # 2 bookmarks
    cost_per_bookmark = 2 # $2
    total_cost_bookmarks = num_bookmarks * cost_per_bookmark

    # L4
    total_purchase_cost = total_cost_posters + total_cost_notebooks + total_cost_bookmarks

    # L5
    num_bills = 2 # two $20 bills
    bill_denomination = 20 # $20 bills
    total_payment = num_bills * bill_denomination

    # L6
    money_left_over = total_payment - total_purchase_cost

    # FA
    answer = money_left_over
    return answer