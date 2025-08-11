from fractions import Fraction

def solve():
    """Index: 733.
    Returns: the total number of seashells remaining.
    """
    # L1
    henry_seashells = 11 # Henry collected 11
    paul_seashells = 24 # Paul 24
    henry_paul_total = henry_seashells + paul_seashells

    # L2
    initial_total_seashells = 59 # initially collected 59 seashells in total
    leo_seashells = initial_total_seashells - henry_paul_total

    # L3
    quarter_fraction = Fraction(1, 4) # a quarter of his collection
    seashells_given_away = leo_seashells * quarter_fraction

    # L4
    remaining_seashells = initial_total_seashells - seashells_given_away

    # FA
    answer = remaining_seashells
    return answer