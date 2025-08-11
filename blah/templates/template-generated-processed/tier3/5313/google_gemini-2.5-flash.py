from fractions import Fraction

def solve():
    """Index: 5313.
    Returns: the number of pieces of cake each sister received.
    """
    # L1
    eaten_percentage = Fraction(60, 100) # 60% of the cake's pieces
    total_cake_pieces = 240 # 240 cake pieces
    pieces_eaten = eaten_percentage * total_cake_pieces

    # L2
    remaining_pieces = total_cake_pieces - pieces_eaten

    # L3
    num_sisters = 3 # among his three sisters
    pieces_per_sister = remaining_pieces / num_sisters

    # FA
    answer = pieces_per_sister
    return answer