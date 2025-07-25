from fractions import Fraction

def solve():
    """Index: 425.
    Returns: the number of points Paislee needed to tie the game.
    """
    # L1
    calvin_points = 500 # Calvin had scored 500 points
    paislee_ratio = Fraction(3, 4) # Paislee 3/4 times as many points as Calvin
    paislee_points = paislee_ratio * calvin_points

    # L2
    points_needed_to_tie = calvin_points - paislee_points

    # FA
    answer = points_needed_to_tie
    return answer