def solve():
    """Index: 2873.
    Returns: the number of newborns Diana will be shopping for.
    """
    # L1
    toddlers = 6 # there are 6 toddlers
    teenagers_per_toddler = 5 # five times as many teenagers as toddlers
    teenagers = teenagers_per_toddler * toddlers

    # L2
    total_children = 40 # all the 40 children
    newborns = total_children - teenagers - toddlers

    # FA
    answer = newborns
    return answer