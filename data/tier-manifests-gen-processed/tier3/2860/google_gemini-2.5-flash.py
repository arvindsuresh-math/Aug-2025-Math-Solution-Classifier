def solve():
    """Index: 2860.
    Returns: the average number of goals scored per game.
    """
    # L1
    num_pizzas = 6 # he bought 6 pizzas
    slices_per_pizza = 12 # A large pizza has 12 slices
    total_goals = num_pizzas * slices_per_pizza

    # L2
    num_games = 8 # the team had 8 games
    average_goals_per_game = total_goals / num_games

    # FA
    answer = average_goals_per_game
    return answer