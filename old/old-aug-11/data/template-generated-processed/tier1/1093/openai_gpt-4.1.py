def solve():
    """Index: 1093.
    Returns: the total combined number of thumbtacks from the three full cans.
    """
    # L1
    tacks_per_board = 3 # one thumbtack from each of the three cans
    boards_tested = 120 # tested 120 boards
    tacks_used = tacks_per_board * boards_tested

    # L2
    cans = 3 # three cans
    tacks_remaining_per_can = 30 # 30 tacks remaining in each can
    tacks_remaining = cans * tacks_remaining_per_can

    # L3
    total_tacks = tacks_used + tacks_remaining

    # FA
    answer = total_tacks
    return answer