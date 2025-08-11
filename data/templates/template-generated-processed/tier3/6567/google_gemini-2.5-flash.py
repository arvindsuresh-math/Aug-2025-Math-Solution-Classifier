def solve():
    """Index: 6567.
    Returns: the number of days the notebooks will last.
    """
    # L1
    num_notebooks = 5 # 5 notebooks
    pages_per_notebook = 40 # 40 pages each
    total_pages = num_notebooks * pages_per_notebook

    # L2
    pages_per_day = 4 # 4 pages per day
    days_last = total_pages / pages_per_day

    # FA
    answer = days_last
    return answer