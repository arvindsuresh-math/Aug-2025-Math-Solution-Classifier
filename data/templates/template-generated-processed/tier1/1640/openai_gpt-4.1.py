def solve():
    """Index: 1640.
    Returns: the number of pieces of candy Jafari started with.
    """
    # L1
    taquon_candy = 171 # Taquon had 171 pieces of candy
    mack_candy = 171 # Mack had 171 pieces of candy
    taquon_mack_total = taquon_candy + mack_candy

    # L2
    total_candy = 418 # they had 418 pieces of candy
    jafari_candy = total_candy - taquon_mack_total

    # FA
    answer = jafari_candy
    return answer