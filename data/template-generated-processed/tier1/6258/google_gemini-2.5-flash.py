def solve():
    """Index: 6258.
    Returns: the total number of listens the song will have by the end of the year according to the solution's calculation.
    """
    # L1
    current_listens = 60000 # currently has 60,000 listens
    doubling_factor = 2 # number of listens per month doubles
    listens_month1 = current_listens * doubling_factor

    # L2
    listens_month2 = listens_month1 * doubling_factor

    # L3
    listens_month3 = listens_month2 * doubling_factor

    # L4
    total_listens = current_listens + listens_month1 + listens_month2 + listens_month3

    # FA
    answer = total_listens
    return answer