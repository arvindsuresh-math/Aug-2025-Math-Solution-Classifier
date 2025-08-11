from fractions import Fraction

def solve():
    """Index: 2672.
    Returns: the number of pizza pieces that remained.
    """
    # L1
    total_people = 15 # In a house of 15
    pizza_eaters_fraction = Fraction(3, 5) # 3/5 of the people eat pizza
    people_eating_pizza = pizza_eaters_fraction * total_people

    # L2
    pieces_per_person = 4 # each person eating pizza took 4 pieces
    total_pieces_taken = pieces_per_person * people_eating_pizza

    # L3
    initial_pizza_pieces = 50 # Aviana brought pizza with 50 pieces
    remaining_pizza_pieces = initial_pizza_pieces - total_pieces_taken

    # FA
    answer = remaining_pizza_pieces
    return answer