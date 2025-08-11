def solve():
    """Index: 2467.
    Returns: the total number of games won by Betsy, Helen, and Susan combined.
    """
    # L1
    betsy_games = 5 # Betsy won 5 games
    helen_multiplier = 2 # Helen won twice as many as Betsy
    helen_games = helen_multiplier * betsy_games

    # L2
    susan_multiplier = 3 # Susan won three times as many as Betsy
    susan_games = susan_multiplier * betsy_games

    # L3
    total_games = betsy_games + helen_games + susan_games

    # FA
    answer = total_games
    return answer