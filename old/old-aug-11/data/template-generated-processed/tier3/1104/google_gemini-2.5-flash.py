def solve():
    """Index: 1104.
    Returns: the number of people who bought tickets but did not go to the concert.
    """
    # L1
    total_tickets_sold = 900 # Nine hundred tickets were sold
    fraction_came_before_numerator = 3 # Three-fourths of those who bought the ticket came before the start
    fraction_came_before_denominator = 4 # Three-fourths of those who bought the ticket came before the start
    came_before_start = total_tickets_sold * fraction_came_before_numerator / fraction_came_before_denominator

    # L2
    did_not_come_before_start = total_tickets_sold - came_before_start

    # L3
    fraction_came_after_first_song_numerator = 5 # Five-ninths of the remaining came few minutes after the first song
    fraction_came_after_first_song_denominator = 9 # Five-ninths of the remaining came few minutes after the first song
    came_after_first_song = did_not_come_before_start * fraction_came_after_first_song_numerator / fraction_came_after_first_song_denominator

    # L4
    arrived_middle_part = 80 # Eighty people arrived during the middle part
    came_late_total = came_after_first_song + arrived_middle_part

    # L5
    did_not_go = did_not_come_before_start - came_late_total

    # FA
    answer = did_not_go
    return answer