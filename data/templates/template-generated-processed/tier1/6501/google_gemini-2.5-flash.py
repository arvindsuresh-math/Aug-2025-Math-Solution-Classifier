def solve():
    """Index: 6501.
    Returns: the number of pieces of clothing Amara has remaining.
    """
    # L1
    donated_to_first_orphanage = 5 # donated 5 to one orphanage home
    multiplier_for_second_orphanage = 3 # triple that to another orphanage home
    donated_to_second_orphanage_value = donated_to_first_orphanage * multiplier_for_second_orphanage
    total_donated = donated_to_first_orphanage + donated_to_second_orphanage_value

    # L2
    initial_clothing_pieces = 100 # Amara had 100 pieces of clothing
    remaining_after_donating = initial_clothing_pieces - total_donated

    # L3
    thrown_away = 15 # throw away 15 of her old clothes
    remaining_after_throwing_away = remaining_after_donating - thrown_away

    # FA
    answer = remaining_after_throwing_away
    return answer