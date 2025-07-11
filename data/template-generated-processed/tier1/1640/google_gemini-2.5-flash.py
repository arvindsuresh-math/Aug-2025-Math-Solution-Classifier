def solve():
    """Index: 1640.
    Returns: the number of pieces of candy Jafari started with.
    """
    # L1
    num_people_taquon_mack = 2 # Taquon, Mack
    candy_per_person_taquon_mack = 171 # each had 171 pieces of candy
    taquon_mack_total_candy = num_people_taquon_mack * candy_per_person_taquon_mack

    # L2
    total_candy_all = 418 # they had 418 pieces of candy
    jafari_candy = total_candy_all - taquon_mack_total_candy

    # FA
    answer = jafari_candy
    return answer