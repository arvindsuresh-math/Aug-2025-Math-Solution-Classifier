def solve():
    """Index: 5266.
    Returns: the number of books Kenny can buy.
    """
    # L1
    lawns_mowed = 35 # mowed 35 lawns
    charge_per_lawn = 15 # charges $15 per lawn
    total_earnings = lawns_mowed * charge_per_lawn

    # L2
    num_video_games = 5 # 5 video-games he really wants
    cost_per_video_game = 45 # video-games are $45 each
    cost_of_video_games = num_video_games * cost_per_video_game

    # L3
    money_left_after_games = total_earnings - cost_of_video_games

    # L4
    cost_per_book = 5 # books are $5 each
    num_books = money_left_after_games / cost_per_book

    # FA
    answer = num_books
    return answer