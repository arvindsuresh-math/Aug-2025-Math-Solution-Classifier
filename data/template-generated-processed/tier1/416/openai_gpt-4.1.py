def solve():
    """Index: 416.
    Returns: the depth of the river in feet by mid-July.
    """
    # L1
    may_depth = 5 # river is five feet deep
    june_increase = 10 # river is 10 feet deeper than mid-May
    june_depth = may_depth + june_increase

    # L2
    july_multiplier = 3 # river is three times deeper than mid-June
    july_depth = june_depth * july_multiplier

    # FA
    answer = july_depth
    return answer