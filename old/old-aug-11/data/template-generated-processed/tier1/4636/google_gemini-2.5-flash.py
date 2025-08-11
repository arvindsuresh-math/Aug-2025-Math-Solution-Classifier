def solve():
    """Index: 4636.
    Returns: the number of biscuits Randy is left with.
    """
    # L1
    randy_initial_biscuits = 32 # Randy had 32 biscuits
    father_gift = 13 # His father gave him 13 biscuits
    biscuits_after_father = randy_initial_biscuits + father_gift

    # L2
    mother_gift = 15 # His mother gave him 15 biscuits
    biscuits_after_mother = biscuits_after_father + mother_gift

    # L3
    brother_ate = 20 # Randy’s brother ate 20 of these biscuits
    biscuits_remaining = biscuits_after_mother - brother_ate

    # FA
    answer = biscuits_remaining
    return answer