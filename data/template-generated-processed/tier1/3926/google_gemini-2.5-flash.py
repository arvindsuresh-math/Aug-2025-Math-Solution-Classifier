def solve():
    """Index: 3926.
    Returns: the number of sheets of paper Fred has left.
    """
    # L1
    initial_sheets = 212 # 212 sheets of paper
    received_sheets = 307 # another 307 sheets of paper
    total_after_receiving = initial_sheets + received_sheets

    # L2
    gave_sheets = 156 # gave Charles 156 sheets of paper
    sheets_left = total_after_receiving - gave_sheets

    # FA
    answer = sheets_left
    return answer