def solve():
    """Index: 2043.
    Returns: the difference in total books read between Brad and William across two months.
    """
    # L1
    william_last_month = 6 # William read 6 books last month
    brad_multiplier_last_month = 3 # Brad read thrice as many books as William did
    brad_last_month = brad_multiplier_last_month * william_last_month

    # L2
    brad_this_month = 8 # Brad, who read 8 books (this month)
    william_multiplier_this_month = 2 # Williams read twice as much as Brad
    william_this_month = william_multiplier_this_month * brad_this_month

    # L3
    brad_total = brad_last_month + brad_this_month

    # L4
    william_total = william_last_month + william_this_month

    # L5
    difference = brad_total - william_total

    # FA
    answer = difference
    return answer