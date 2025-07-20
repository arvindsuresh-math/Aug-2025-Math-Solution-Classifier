from fractions import Fraction

def solve():
    """Index: 7202.
    Returns: the number of marbles remaining in the pile.
    """
    # L1
    chris_marbles = 12 # Chris has twelve marbles
    ryan_marbles = 28 # Ryan has twenty-eight marbles
    total_marbles_initial = chris_marbles + ryan_marbles

    # L2
    fraction_taken = Fraction(1, 4) # 1/4 of marbles
    marbles_per_person = fraction_taken * total_marbles_initial

    # L3
    total_marbles_taken = marbles_per_person + marbles_per_person

    # L4
    marbles_remaining = total_marbles_initial - total_marbles_taken

    # FA
    answer = marbles_remaining
    return answer