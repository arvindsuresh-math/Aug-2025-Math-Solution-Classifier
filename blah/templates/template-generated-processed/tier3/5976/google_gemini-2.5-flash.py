def solve():
    """Index: 5976.
    Returns: the number of 5 inch subs Venus needs to buy.
    """
    # L1
    num_eight_inch_subs = 2 # buys two 8 inch subs
    length_eight_inch_sub = 8 # 8 inch subs
    total_length_eight_inch_subs = num_eight_inch_subs * length_eight_inch_sub

    # L2
    total_sub_needed = 81 # needs 81 inches of sub
    remaining_sub_needed = total_sub_needed - total_length_eight_inch_subs

    # L3
    length_five_inch_sub = 5 # 5 inch subs
    num_five_inch_subs = remaining_sub_needed / length_five_inch_sub

    # FA
    answer = num_five_inch_subs
    return answer