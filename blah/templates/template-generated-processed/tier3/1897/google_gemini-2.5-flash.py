def solve():
    """Index: 1897.
    Returns: the number of additional minutes to download the game.
    """
    # L1
    total_game_size = 880 # 880 MB game
    downloaded_size = 310 # After downloading 310 MB
    remaining_download_size = total_game_size - downloaded_size

    # L2
    download_speed = 3 # slows to 3 MB/minute
    time_to_download = remaining_download_size / download_speed

    # FA
    answer = time_to_download
    return answer