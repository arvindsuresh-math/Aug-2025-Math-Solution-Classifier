def solve():
    """Index: 1376.
    Returns: the number of yellow leaves collected.
    """
    # L1
    leaves_thursday = 12 # 12 on Thursday
    leaves_friday = 13 # 13 on Friday
    total_leaves = leaves_thursday + leaves_friday

    # L2
    total_percent = 100 # WK
    brown_percent = 20 # 20% are Brown
    green_percent = 20 # 20% are Green
    yellow_percent_num = total_percent - brown_percent - green_percent

    # L3
    yellow_percent_decimal = 0.6 # from solution text: .6
    yellow_leaves_count = total_leaves * yellow_percent_decimal

    # FA
    answer = yellow_leaves_count
    return answer