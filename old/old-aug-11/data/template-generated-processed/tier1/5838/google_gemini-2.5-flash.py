def solve():
    """Index: 5838.
    Returns: the depth of Peter's pond.
    """
    # L3
    mark_pond_depth = 19 # Mark’s pond is 19 feet deep
    deeper_than_three_times = 4 # 4 feet deeper than 3 times Peter’s pond
    three_times_peter_depth = mark_pond_depth - deeper_than_three_times

    # L5
    divisor_for_peter_depth = 3 # 3 times Peter’s pond
    peter_pond_depth = three_times_peter_depth / divisor_for_peter_depth

    # FA
    answer = peter_pond_depth
    return answer