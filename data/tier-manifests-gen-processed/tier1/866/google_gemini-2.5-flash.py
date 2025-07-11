def solve():
    """Index: 866.
    Returns: the total number of notes put into the complaints and compliments bins.
    """
    # L1
    num_rows_red_notes = 5 # 5 rows
    notes_per_row_red_notes = 6 # 6 notes in each row
    total_red_notes = num_rows_red_notes * notes_per_row_red_notes

    # L2
    blue_notes_per_red_note = 2 # 2 blue notes under each of the red notes
    blue_notes_under_red = blue_notes_per_red_note * total_red_notes

    # L3
    scattered_blue_notes = 10 # another 10 blue notes scattered at the bottom of the board
    total_blue_notes = blue_notes_under_red + scattered_blue_notes

    # L4
    total_notes = total_red_notes + total_blue_notes

    # FA
    answer = total_notes
    return answer