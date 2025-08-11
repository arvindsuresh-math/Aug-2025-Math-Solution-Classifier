def solve():
    """Index: 4037.
    Returns: the number of more cats Susan has than Bob after the exchange.
    """
    # L1
    susan_initial_cats = 21 # Susan has 21 cats
    cats_given_away = 4 # gives Robert 4 of her cats
    susan_after_giving = susan_initial_cats - cats_given_away

    # L2
    bob_initial_cats = 3 # Bob has 3 cats
    difference = susan_after_giving - bob_initial_cats

    # FA
    answer = difference
    return answer