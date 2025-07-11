def solve():
    """Index: 693.
    Returns: the number of roses Ian kept.
    """
    # L1
    roses_to_mother = 6 # gave six roses to his mother
    roses_to_grandmother = 9 # nine roses to his grandmother
    roses_to_sister = 4 # four roses to his sister
    total_given = roses_to_mother + roses_to_grandmother + roses_to_sister

    # L2
    total_roses = 20 # Ian had twenty roses
    roses_kept = total_roses - total_given

    # FA
    answer = roses_kept
    return answer