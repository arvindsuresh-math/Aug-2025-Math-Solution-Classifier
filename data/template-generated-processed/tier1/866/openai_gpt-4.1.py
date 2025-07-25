def solve():
    """Index: 866.
    Returns: the total number of notes put into the complaints and compliments bins.
    """
    # L1
    num_rows_red = 5 # 5 rows with 6 notes in each row
    notes_per_row_red = 6 # 6 notes in each row
    total_red_notes = num_rows_red * notes_per_row_red

    # L2
    blue_per_red = 2 # 2 blue notes under each of the red notes
    blue_under_red = blue_per_red * total_red_notes

    # L3
    scattered_blue = 10 # another 10 blue notes scattered at the bottom
    total_blue_notes = blue_under_red + scattered_blue

    # L4
    total_notes = total_red_notes + total_blue_notes

    # FA
    answer = total_notes
    return answer