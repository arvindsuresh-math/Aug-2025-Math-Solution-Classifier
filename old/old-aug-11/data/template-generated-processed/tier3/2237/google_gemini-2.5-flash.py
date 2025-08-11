def solve():
    """Index: 2237.
    Returns: the amount of money Mary had left.
    """
    # L1
    initial_money = 100 # her brother surprised her with $100
    video_game_divisor = 4 # a quarter of it
    video_game_cost = initial_money / video_game_divisor

    # L2
    money_after_video_game = initial_money - video_game_cost

    # L3
    goggles_divisor = 5 # a fifth of what was left
    goggles_cost = money_after_video_game / goggles_divisor

    # L4
    money_left = money_after_video_game - goggles_cost

    # FA
    answer = money_left
    return answer