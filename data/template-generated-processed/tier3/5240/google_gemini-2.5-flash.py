from fractions import Fraction

def solve():
    """Index: 5240.
    Returns: the total number of video games Theresa has.
    """
    # L1
    julia_fraction = Fraction(1, 3) # Julia has a third as many video games
    tory_games = 6 # Tory has 6 video games
    julia_games = julia_fraction * tory_games

    # L2
    theresa_multiplier = 3 # thrice as many video games
    theresa_addition = 5 # 5 more than
    theresa_games = theresa_multiplier * julia_games + theresa_addition

    # FA
    answer = theresa_games
    return answer