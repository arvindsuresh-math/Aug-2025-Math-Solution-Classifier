def solve():
    """Index: 5277.
    Returns: the number of pies they can make.
    """
    # L1
    total_apples = 34 # picked 34 apples
    unripe_apples = 6 # 6 of the apples they picked are not ripe
    ripe_apples = total_apples - unripe_apples

    # L2
    apples_per_pie = 4 # Each apple pie needs 4 apples
    num_pies = ripe_apples / apples_per_pie

    # FA
    answer = num_pies
    return answer