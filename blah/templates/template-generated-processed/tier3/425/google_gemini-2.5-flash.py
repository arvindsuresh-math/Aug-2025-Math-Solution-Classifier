from fractions import Fraction

def solve():
    """Index: 425.
    Returns: the number of points Paislee needed to score to tie the game.
    """
    # L1
    calvin_score = 500 # Calvin had scored 500 points
    paislee_fraction = Fraction(3, 4) # Paislee 3/4 times as many points as Calvin
    paislee_score = paislee_fraction * calvin_score

    # L2
    points_needed_to_tie = calvin_score - paislee_score

    # FA
    answer = points_needed_to_tie
    return answer