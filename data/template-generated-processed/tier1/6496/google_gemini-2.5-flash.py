def solve():
    """Index: 6496.
    Returns: the total number of pieces of mail handled in six months.
    """
    # L1
    letters_per_day = 60 # 60 letters
    packages_per_day = 20 # 20 packages
    total_pieces_per_day = letters_per_day + packages_per_day

    # L2
    days_per_month = 30 # all the months have 30 days
    pieces_per_month = total_pieces_per_day * days_per_month

    # L3
    num_months = 6 # in six months
    total_pieces_six_months = pieces_per_month * num_months

    # FA
    answer = total_pieces_six_months
    return answer