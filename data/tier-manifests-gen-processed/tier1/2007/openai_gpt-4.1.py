def solve():
    """Index: 2007.
    Returns: the total number of lambs Merry and her brother have.
    """
    # L1
    merry_lambs = 10 # Merry is taking care of 10 lambs
    brother_more_than_merry = 3 # Her brother takes care of 3 more lambs than Merry
    brother_lambs = merry_lambs + brother_more_than_merry

    # L2
    total_lambs = merry_lambs + brother_lambs

    # FA
    answer = total_lambs
    return answer