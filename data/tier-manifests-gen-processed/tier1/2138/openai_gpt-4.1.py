def solve():
    """Index: 2138.
    Returns: the total number of tables the carpenter made in two months.
    """
    # L1
    tables_this_month = 10 # made ten tables for this month
    fewer_tables_last_month = 3 # made three fewer tables than this month
    tables_last_month = tables_this_month - fewer_tables_last_month

    # L2
    total_tables = tables_this_month + tables_last_month

    # FA
    answer = total_tables
    return answer