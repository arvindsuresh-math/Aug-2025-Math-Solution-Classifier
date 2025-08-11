from fractions import Fraction

def solve():
    """Index: 7374.
    Returns: the number of pieces of pumpkin pie left.
    """
    # L1
    sold_pies = 1 # sold 1 whole pumpkin pie
    gave_pies = 1 # gave 1 whole pumpkin pie to her friend
    pies_sold_and_given = sold_pies + gave_pies

    # L2
    initial_pies = 4 # Grace baked 4 whole pumpkin pies
    remaining_whole_pies = initial_pies - pies_sold_and_given

    # L3
    pieces_per_pie = 6 # each sliced into 6 pieces
    total_pieces_made = remaining_whole_pies * pieces_per_pie

    # L4
    fraction_eaten = Fraction(2, 3) # ate 2/3 pieces
    pieces_eaten = total_pieces_made * fraction_eaten

    # L5
    pieces_left = total_pieces_made - pieces_eaten

    # FA
    answer = pieces_left
    return answer