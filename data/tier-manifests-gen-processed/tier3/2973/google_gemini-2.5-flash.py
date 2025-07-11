def solve():
    """Index: 2973.
    Returns: the number of stuffies Janet got.
    """
    # L1
    total_stuffies = 60 # Jean has 60 stuffies
    kept_denominator = 3 # 1/3 of them
    stuffies_kept = total_stuffies / kept_denominator

    # L2
    stuffies_given_away = total_stuffies - stuffies_kept

    # L3
    janet_share_denominator = 4 # 1/4 of what she gave away
    janet_stuffies = stuffies_given_away / janet_share_denominator

    # FA
    answer = janet_stuffies
    return answer