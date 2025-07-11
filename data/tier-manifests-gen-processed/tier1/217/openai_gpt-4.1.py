def solve():
    """Index: 217.
    Returns: Anne's age when Maude is 8 and Emile is six times as old as Maude, and Anne is twice as old as Emile.
    """
    # L1
    maude_age = 8 # Maude will be 8 years old
    emile_multiplier = 6 # Emile will be six times as old as Maude
    emile_age = emile_multiplier * maude_age

    # L2
    anne_multiplier = 2 # Anne is two times as old as Emile
    anne_age = anne_multiplier * emile_age

    # FA
    answer = anne_age
    return answer