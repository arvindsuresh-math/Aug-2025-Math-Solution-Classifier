def solve():
    """Index: 497.
    Returns: the amount the player gets paid for the week.
    """
    # L1
    game1_points = 30 # in the first game he scored 30 points
    game2_points = 28 # in the second game he scored 28 points
    game3_points = 32 # In the third game he scored 32 points
    game4_points = 34 # In the fourth game he scored 34 points
    game5_points = 26 # in the fifth game he scored 26 points
    total_points = game1_points + game2_points + game3_points + game4_points + game5_points

    # L2
    number_of_games = 5 # first game, second game, third game, fourth game, fifth game
    average_points_per_game = total_points / number_of_games

    # L3
    payment_high = 10000 # He gets $10,000 if he averages 30 or more points a game
    payment_threshold = 30 # averages 30 or more points a game
    weekly_payment = payment_high

    # FA
    answer = weekly_payment
    return answer