def solve():
    """Index: 6536.
    Returns: how many more people watched the games this week than last week.
    """
    # L1
    second_game_watchers = 80 # eighty people watched the second game
    fewer_first_game = 20 # 20 fewer people watched the first game than the second game
    first_game_watchers = second_game_watchers - fewer_first_game

    # L2
    more_third_game = 15 # 15 more people watched the third than the second game
    third_game_watchers = second_game_watchers + more_third_game

    # L3
    this_week_total = second_game_watchers + first_game_watchers + third_game_watchers

    # L4
    last_week_total = 200 # a total of 200 people who watched the games last week
    difference_this_vs_last_week = this_week_total - last_week_total

    # FA
    answer = difference_this_vs_last_week
    return answer