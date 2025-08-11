def solve():
    """Index: 3819.
    Returns: the number of necklaces Becky owns now.
    """
    # L1
    initial_necklaces = 50 # 50 necklaces in her jewelry collection
    broken_necklaces = 3 # 3 of the necklaces have broken beads
    after_broken = initial_necklaces - broken_necklaces

    # L2
    new_necklaces = 5 # buys 5 new necklaces
    after_buying = after_broken + new_necklaces

    # L3
    given_away = 15 # give 15 of her old necklaces to her friends
    final_necklaces = after_buying - given_away

    # FA
    answer = final_necklaces
    return answer