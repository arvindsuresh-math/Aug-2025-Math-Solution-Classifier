def solve():
    """Index: 2111.
    Returns: the total time before James can play the main game.
    """
    # L1
    download_time = 10 # James spends 10 minutes downloading a game
    half_divisor = 2 # half as long installing it
    install_time = download_time / half_divisor

    # L2
    combined_download_install_time = install_time + download_time

    # L3
    triple_multiplier = 3 # triple that combined amount of time
    tutorial_time = combined_download_install_time * triple_multiplier

    # L4
    total_time = tutorial_time + combined_download_install_time

    # FA
    answer = total_time
    return answer