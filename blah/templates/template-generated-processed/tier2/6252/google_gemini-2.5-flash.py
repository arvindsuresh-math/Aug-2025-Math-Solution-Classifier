def solve():
    """Index: 6252.
    Returns: the total number of times Jenny has won board games with her two friends.
    """
    # L1
    games_played_mark = 10 # played him 10 times
    mark_wins_against_jenny = 1 # Mark has only won once
    jenny_wins_against_mark = games_played_mark - mark_wins_against_jenny

    # L2
    games_played_jill = games_played_mark * 2

    # L3
    jill_win_percentage = 0.75 # Jill has won 75% of them
    jill_wins_against_jenny = games_played_jill * jill_win_percentage

    # L4
    jenny_wins_against_jill = games_played_jill - jill_wins_against_jenny

    # L5
    total_jenny_wins = jenny_wins_against_jill + jenny_wins_against_mark

    # FA
    answer = total_jenny_wins
    return answer