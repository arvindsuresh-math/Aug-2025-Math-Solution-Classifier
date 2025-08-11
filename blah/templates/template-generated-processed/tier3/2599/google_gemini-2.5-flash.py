def solve():
    """Index: 2599.
    Returns: the total number of wicks cut.
    """
    # L1
    string_length_feet = 15 # a 15-foot spool
    inches_per_foot = 12 # WK
    string_length_inches = string_length_feet * inches_per_foot

    # L2
    wick_length_1 = 6 # 6-inch
    wick_length_2 = 12 # 12-inch
    pair_length = wick_length_1 + wick_length_2

    # L3
    num_pairs = string_length_inches / pair_length

    # L4
    wicks_per_pair = 2 # WK
    total_wicks = num_pairs * wicks_per_pair

    # FA
    answer = total_wicks
    return answer