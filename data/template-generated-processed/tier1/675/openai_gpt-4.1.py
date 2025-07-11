def solve():
    """Index: 675.
    Returns: the percentage by which losing both lawsuits is more likely than winning both.
    """
    # L1
    win_first_pct = 30 # 30% chance of paying out $5,000,000 upon a win
    total_pct = 100 # WK
    lose_first_pct = total_pct - win_first_pct

    # L2
    lose_second_pct = 50 # 50% chance of paying out $1,000,000 if Andy loses
    both_lose_pct = lose_first_pct * lose_second_pct // total_pct

    # L3
    win_second_pct = 50 # 50% chance of paying out $2,000,000 if he wins
    both_win_pct = win_first_pct * win_second_pct // total_pct

    # L4
    difference_pct = both_lose_pct - both_win_pct

    # FA
    answer = difference_pct
    return answer