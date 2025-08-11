def solve():
    """Index: 2873.
    Returns: the number of newborns Diana will be shopping for.
    """
    # L1
    toddlers = 6 # 6 toddlers
    teenager_multiplier = 5 # five times as many teenagers as toddlers
    teenagers = teenager_multiplier * toddlers

    # L2
    total_children = 40 # 40 children
    newborns = total_children - teenagers - toddlers

    # FA
    answer = newborns
    return answer