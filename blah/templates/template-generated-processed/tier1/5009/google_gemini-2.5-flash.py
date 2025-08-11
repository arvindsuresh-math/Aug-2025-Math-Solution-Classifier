def solve():
    """Index: 5009.
    Returns: the total cost of Lea's purchases.
    """
    # L1
    num_binders = 3 # three binders
    cost_per_binder = 2 # $2
    cost_binders = num_binders * cost_per_binder

    # L2
    num_notebooks = 6 # six notebooks
    cost_per_notebook = 1 # $1
    cost_notebooks = num_notebooks * cost_per_notebook

    # L3
    cost_book = 16 # one book for $16
    total_cost = cost_book + cost_binders + cost_notebooks

    # FA
    answer = total_cost
    return answer