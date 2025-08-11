def solve():
    """Index: 4564.
    Returns: the number of hoodies Fiona owns.
    """
    # L4
    total_hoodies = 8 # Between the two of them, they own eight hoodies
    casey_more_than_fiona = 2 # Casey owns two more than Fiona
    two_times_fiona_hoodies = total_hoodies - casey_more_than_fiona

    # L5
    multiplier_for_H = 2 # WK (from 2H)
    fiona_hoodies = two_times_fiona_hoodies / multiplier_for_H

    # FA
    answer = fiona_hoodies
    return answer