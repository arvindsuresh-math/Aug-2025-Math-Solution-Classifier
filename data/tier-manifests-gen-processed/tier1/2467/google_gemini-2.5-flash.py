def solve():
    """Index: 2467.
    Returns: the total number of games won by Betsy, Helen, and Susan.
    """
    # L1
    betsy_wins = 5 # Betsy won 5 games of Monopoly
    helen_multiplier = 2 # twice as many as Betsy
    helen_wins = helen_multiplier * betsy_wins

    # L2
    susan_multiplier = 3 # three times as many as Betsy
    susan_wins = susan_multiplier * betsy_wins

    # L3
    total_wins = betsy_wins + helen_wins + susan_wins

    # FA
    answer = total_wins
    return answer