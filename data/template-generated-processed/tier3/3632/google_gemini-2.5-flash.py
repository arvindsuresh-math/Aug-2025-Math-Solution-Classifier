def solve():
    """Index: 3632.
    Returns: the cost per page in cents.
    """
    # L1
    num_notebooks = 2 # 2 notebooks
    pages_per_notebook = 50 # 50 pages each
    total_pages = num_notebooks * pages_per_notebook

    # L2
    cost_dollars = 5 # $5
    cents_per_dollar = 100 # WK
    total_cost_cents = cost_dollars * cents_per_dollar

    # L3
    cost_per_page_cents = total_cost_cents / total_pages

    # FA
    answer = cost_per_page_cents
    return answer