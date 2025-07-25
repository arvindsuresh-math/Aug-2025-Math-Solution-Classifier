def solve():
    """Index: 3659.
    Returns: the total number of video games Radhika owns.
    """
    # L1
    christmas_games = 12 # 12 new video games
    birthday_games = 8 # 8 more video games
    games_given_as_gifts = christmas_games + birthday_games

    # L2
    owned_fraction_denominator = 2 # 1/2 the number of games
    games_already_owned = games_given_as_gifts / owned_fraction_denominator

    # L3
    total_games = games_given_as_gifts + games_already_owned

    # FA
    answer = total_games
    return answer