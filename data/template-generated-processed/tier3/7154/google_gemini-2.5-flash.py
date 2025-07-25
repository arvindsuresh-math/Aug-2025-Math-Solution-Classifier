def solve():
    """Index: 7154.
    Returns: the total number of pairs of pants and dresses Isabella bought.
    """
    # L1
    alexis_pants = 21 # Alexis bought 21 pairs of pants
    times_more = 3 # Alexis bought 3 times more pants and dresses than Isabella
    isabella_pants = alexis_pants / times_more

    # L2
    alexis_dresses = 18 # and 18 dresses
    isabella_dresses = alexis_dresses / times_more

    # L3
    total_isabella_items = isabella_pants + isabella_dresses

    # FA
    answer = total_isabella_items
    return answer