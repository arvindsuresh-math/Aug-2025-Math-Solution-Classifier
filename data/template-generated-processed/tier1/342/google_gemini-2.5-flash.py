def solve():
    """Index: 342.
    Returns: the total time Mark was on the sideline.
    """
    # L1
    first_play_time = 20 # played 20 minutes
    second_play_time = 35 # played for another 35 minutes
    total_play_time = first_play_time + second_play_time

    # L2
    total_game_duration = 90 # 90-minute soccer game
    sideline_time = total_game_duration - total_play_time

    # FA
    answer = sideline_time
    return answer