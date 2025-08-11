def solve():
    """Index: 342.
    Returns: the number of minutes Mark was on the sideline during the game.
    """
    # L1
    first_play = 20 # Mark played 20 minutes
    second_play = 35 # played for another 35 minutes
    total_played = first_play + second_play

    # L2
    total_game = 90 # 90-minute soccer game
    sideline_time = total_game - total_played

    # FA
    answer = sideline_time
    return answer