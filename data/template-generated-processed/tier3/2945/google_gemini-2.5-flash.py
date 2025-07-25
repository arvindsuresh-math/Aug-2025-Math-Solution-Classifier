def solve():
    """Index: 2945.
    Returns: the total duration of the chess match in minutes.
    """
    # L1
    total_moves = 30 # The match ends after 30 moves
    num_players = 2 # WK
    moves_per_player = total_moves / num_players

    # L2
    polly_avg_seconds_per_move = 28 # Polly takes an average of 28 seconds per move
    polly_total_seconds = moves_per_player * polly_avg_seconds_per_move

    # L3
    peter_avg_seconds_per_move = 40 # Peter takes an average of 40 seconds per move
    peter_total_seconds = moves_per_player * peter_avg_seconds_per_move

    # L4
    total_seconds_match = polly_total_seconds + peter_total_seconds

    # L5
    seconds_per_minute = 60 # WK
    total_minutes_match = total_seconds_match / seconds_per_minute

    # FA
    answer = total_minutes_match
    return answer