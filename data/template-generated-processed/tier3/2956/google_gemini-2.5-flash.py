from fractions import Fraction

def solve():
    """Index: 2956.
    Returns: the number of times Cyrus missed the shots.
    """
    # L1
    attempted_shots = 20 # He attempted twenty shots
    made_percentage = Fraction(80, 100) # exactly eighty percent of the shots
    shots_made = attempted_shots * made_percentage

    # L2
    shots_missed = attempted_shots - shots_made

    # FA
    answer = shots_missed
    return answer