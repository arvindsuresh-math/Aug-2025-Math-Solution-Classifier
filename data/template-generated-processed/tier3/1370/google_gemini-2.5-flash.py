def solve():
    """Index: 1370.
    Returns: the time it will take to free the younger son.
    """
    # L1
    hannah_cut_rate = 8 # Hannah can cut 8 strands per minute
    son_cut_rate = 3 # her son can cut 3 strands per minute
    combined_cut_rate = hannah_cut_rate + son_cut_rate

    # L2
    total_strands = 22 # 22 strands of duct tape
    time_to_free_son = total_strands / combined_cut_rate

    # FA
    answer = time_to_free_son
    return answer