def solve():
    """Index: 4666.
    Returns: the difference in the number of pencils Dana has compared to Marcus.
    """
    # L1
    dana_more_than_jayden = 15 # Dana has 15 more pencils than Jayden
    jayden_pencils = 20 # Jayden has 20 pencils
    dana_pencils = jayden_pencils + dana_more_than_jayden

    # L2
    twice_factor = 2 # twice as much as Marcus
    marcus_pencils = jayden_pencils / twice_factor

    # L3
    difference_dana_marcus = dana_pencils - marcus_pencils

    # FA
    answer = difference_dana_marcus
    return answer