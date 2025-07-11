def solve():
    """Index: 1707.
    Returns: the number of toys in Kamari's box.
    """
    # L1
    anais_more_than_kamari = 30 # Anais has 30 more toys than Kamari
    # L2
    total_toys = 160 # There are 160 toys altogether
    # L4
    two_x = total_toys - anais_more_than_kamari
    # L5
    kamari_toys = two_x // 2
    # FA
    answer = kamari_toys
    return answer