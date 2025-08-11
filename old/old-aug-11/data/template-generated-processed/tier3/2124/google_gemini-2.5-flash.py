def solve():
    """Index: 2124.
    Returns: the amount of money James has left.
    """
    # L1
    weekly_allowance = 10 # James earns $10 per week
    number_of_weeks = 4 # for four weeks
    total_saved_money = weekly_allowance * number_of_weeks

    # L2
    video_game_divisor = 2 # spends half of it
    spent_on_video_game = total_saved_money / video_game_divisor

    # L3
    money_after_game = total_saved_money - spent_on_video_game

    # L4
    book_divisor = 4 # a quarter of what is left
    spent_on_book = money_after_game / book_divisor

    # L5
    money_left = money_after_game - spent_on_book

    # FA
    answer = money_left
    return answer