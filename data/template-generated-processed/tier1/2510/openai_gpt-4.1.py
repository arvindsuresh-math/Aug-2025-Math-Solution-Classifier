def solve():
    """Index: 2510.
    Returns: the amount of money Lindsey had left after all transactions.
    """
    # L1
    saved_september = 50 # saved $50 in September
    saved_october = 37 # saved $37 in October
    saved_november = 11 # $11 in November
    total_saved = saved_september + saved_october + saved_november

    # L2
    threshold = 75 # more than $75
    mom_bonus = 25 # would give Lindsey $25
    total_with_bonus = total_saved + mom_bonus

    # L3
    video_game_cost = 87 # spent $87 on a video game
    remaining = total_with_bonus - video_game_cost

    # FA
    answer = remaining
    return answer