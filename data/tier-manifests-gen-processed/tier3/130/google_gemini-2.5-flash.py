from fractions import Fraction

def solve():
    """Index: 130.
    Returns: the number of seashells Ali had left.
    """
    # L1
    initial_seashells = 180 # He started with 180 seashells
    given_to_friends = 40 # gave away 40 seashells to his friends
    seashells_after_friends = initial_seashells - given_to_friends

    # L2
    given_to_brothers = 30 # gave 30 seashells to his brothers
    seashells_after_brothers = seashells_after_friends - given_to_brothers

    # L3
    sold_fraction = Fraction(1, 2) # sold half of the remaining seashells
    seashells_sold = sold_fraction * seashells_after_brothers

    # L4
    seashells_left = seashells_after_brothers - seashells_sold

    # FA
    answer = seashells_left
    return answer