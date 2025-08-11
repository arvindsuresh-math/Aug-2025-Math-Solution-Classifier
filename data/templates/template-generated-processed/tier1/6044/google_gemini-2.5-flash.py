def solve():
    """Index: 6044.
    Returns: the number of strokes over par Tom was.
    """
    # L1
    average_strokes_per_hole = 4 # average of 4 strokes per hole
    rounds_of_golf = 9 # plays 9 rounds of golf
    total_strokes_taken = average_strokes_per_hole * rounds_of_golf

    # L2
    par_value_per_hole = 3 # The par value per hole is 3
    total_par_strokes = rounds_of_golf * par_value_per_hole

    # L3
    strokes_over_par = total_strokes_taken - total_par_strokes

    # FA
    answer = strokes_over_par
    return answer