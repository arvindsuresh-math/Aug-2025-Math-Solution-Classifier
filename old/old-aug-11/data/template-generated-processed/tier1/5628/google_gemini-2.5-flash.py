def solve():
    """Index: 5628.
    Returns: the total number of toys Mr. Desmond bought.
    """
    # L1
    multiplier = 3 # three times as many toys
    elder_son_toys = 60 # elder son received 60 toys
    younger_son_toys = multiplier * elder_son_toys

    # L2
    total_toys = younger_son_toys + elder_son_toys

    # FA
    answer = total_toys
    return answer