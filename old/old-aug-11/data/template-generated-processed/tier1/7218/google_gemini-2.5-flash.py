def solve():
    """Index: 7218.
    Returns: the number of pieces of gum Adrianna has now.
    """
    # L1
    initial_gum_pieces = 10 # 10 pieces of gum
    bought_gum_pieces = 3 # get 3 more pieces of gum
    gum_after_buying = initial_gum_pieces + bought_gum_pieces

    # L2
    friends_given_gum = 11 # gave out gum to 11 friends
    gum_remaining = gum_after_buying - friends_given_gum

    # FA
    answer = gum_remaining
    return answer