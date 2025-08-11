def solve():
    """Index: 1093.
    Returns: the total combined number of thumbtacks from the three full cans.
    """
    # L1
    num_boards_tested = 120 # tested 120 boards
    tacks_per_board = 3 # one thumbtack from each of the three cans of thumbtacks into every board tested
    tacks_used_total = tacks_per_board * num_boards_tested

    # L2
    tacks_remaining_per_can = 30 # 30 tacks remaining in each of the three cans
    num_cans = 3 # three full cans of thumbtacks
    tacks_remaining_total = num_cans * tacks_remaining_per_can

    # L3
    total_original_tacks = tacks_used_total + tacks_remaining_total

    # FA
    answer = total_original_tacks
    return answer