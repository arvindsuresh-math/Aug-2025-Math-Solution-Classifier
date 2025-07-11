def solve():
    """Index: 2510.
    Returns: the amount of money Lindsey had left.
    """
    # L1
    saved_september = 50 # saved $50 in September
    saved_october = 37 # saved $37 in October
    saved_november = 11 # saved $11 in November
    total_saved_initial = saved_september + saved_october + saved_november

    # L2
    mom_threshold = 75 # saved more than $75
    mom_bonus = 25 # give Lindsey $25
    total_after_bonus = total_saved_initial + mom_bonus

    # L3
    video_game_cost = 87 # spent $87 on a video game
    money_left = total_after_bonus - video_game_cost

    # FA
    answer = money_left
    return answer