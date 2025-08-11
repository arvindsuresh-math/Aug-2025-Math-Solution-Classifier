def solve():
    """Index: 497.
    Returns: the amount James's favorite basketball player gets paid for the week.
    """
    # L1
    game1_points = 30 # first game he scored 30 points
    game2_points = 28 # second game he scored 28 points
    game3_points = 32 # third game he scored 32 points
    game4_points = 34 # fourth game he scored 34 points
    game5_points = 26 # fifth game he scored 26 points
    total_points = game1_points + game2_points + game3_points + game4_points + game5_points

    # L2
    num_games = 5 # five games in the week
    average_points = total_points / num_games

    # L3
    high_pay = 10000 # $10,000 if he averages 30 or more points a game
    low_pay = 8000 # $8,000 if he averages under 30 points a game
    if average_points >= 30:
        pay = high_pay
    else:
        pay = low_pay

    # FA
    answer = pay
    return answer