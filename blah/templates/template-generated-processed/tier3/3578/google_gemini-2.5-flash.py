def solve():
    """Index: 3578.
    Returns: the number of dresses Ana has.
    """
    # L1
    combined_dresses = 48 # combined is 48
    lisa_surplus = 18 # 18 more dresses
    dresses_after_surplus_removal = combined_dresses - lisa_surplus

    # L2
    num_people = 2 # WK
    ana_dresses = dresses_after_surplus_removal / num_people

    # FA
    answer = ana_dresses
    return answer