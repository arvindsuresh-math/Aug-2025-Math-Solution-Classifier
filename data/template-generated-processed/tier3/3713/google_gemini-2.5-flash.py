def solve():
    """Index: 3713.
    Returns: the number of slices of cake that were kept.
    """
    # L1
    total_pieces = 12 # 12 equal pieces
    fraction_denominator = 4 # one-fourth of the cake
    slices_eaten = total_pieces / fraction_denominator

    # L2
    slices_kept = total_pieces - slices_eaten

    # FA
    answer = slices_kept
    return answer