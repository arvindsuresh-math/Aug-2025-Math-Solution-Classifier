def solve():
    """Index: 2965.
    Returns: the number of tennis balls Bertha has after twenty games.
    """
    # L1
    total_games = 20 # After twenty games
    wear_out_frequency = 10 # Every ten games, one of her tennis balls wears out
    balls_worn_out = total_games / wear_out_frequency

    # L2
    lose_frequency = 5 # Every five games, she loses a ball
    balls_lost = total_games / lose_frequency

    # L3
    balls_per_canister = 3 # canister of three balls
    buy_frequency = 4 # Every four games, she buys a canister
    balls_bought = balls_per_canister * total_games / buy_frequency

    # L4
    initial_balls = 2 # She started with two balls
    given_away = 1 # gave one to her partner
    remaining_balls = initial_balls + balls_bought - balls_worn_out - balls_lost - given_away

    # FA
    answer = remaining_balls
    return answer