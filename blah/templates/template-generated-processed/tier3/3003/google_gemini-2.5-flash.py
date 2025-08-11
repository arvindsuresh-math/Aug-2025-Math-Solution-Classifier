def solve():
    """Index: 3003.
    Returns: the depth of the river in mid-May.
    """
    # L1
    mid_july_depth = 45 # If the river is 45 feet deep in mid-July
    times_deeper_than_mid_june = 3 # river is three times deeper than mid-June
    mid_june_depth = mid_july_depth / times_deeper_than_mid_june

    # L2
    deeper_than_mid_may = 10 # river is 10 feet deeper than mid-May
    mid_may_depth = mid_june_depth - deeper_than_mid_may

    # FA
    answer = mid_may_depth
    return answer