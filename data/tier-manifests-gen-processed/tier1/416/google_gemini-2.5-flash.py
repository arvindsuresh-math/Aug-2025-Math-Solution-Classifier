def solve():
    """Index: 416.
    Returns: the depth of the river by mid-July.
    """
    # L1
    mid_may_depth = 5 # five feet deep
    deeper_by_june = 10 # 10 feet deeper than mid-May
    mid_june_depth = mid_may_depth + deeper_by_june

    # L2
    times_deeper_by_july = 3 # three times deeper than mid-June
    mid_july_depth = mid_june_depth * times_deeper_by_july

    # FA
    answer = mid_july_depth
    return answer