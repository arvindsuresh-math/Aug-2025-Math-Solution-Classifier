def solve():
    """Index: 5864.
    Returns: the number of hats Policeman O'Brien now has.
    """
    # L1
    multiplier_twice = 2 # twice as many hats
    simpson_hats = 15 # fire chief Simpson has 15 hats
    twice_simpson_hats = multiplier_twice * simpson_hats

    # L2
    more_than_twice = 5 # 5 more than twice as many hats
    obrien_hats_before_loss = twice_simpson_hats + more_than_twice

    # L3
    lost_hats = 1 # Before he lost one
    obrien_hats_after_loss = obrien_hats_before_loss - lost_hats

    # FA
    answer = obrien_hats_after_loss
    return answer