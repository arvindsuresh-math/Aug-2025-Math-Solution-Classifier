def solve():
    """Index: 2446.
    Returns: the total number of skips Bob and Jim got.
    """
    # L1
    bob_skips_per_rock = 12 # Bob can skip a rock 12 times
    num_rocks_skipped = 10 # they each skipped 10 rocks
    bob_total_skips = bob_skips_per_rock * num_rocks_skipped

    # L2
    jim_skips_per_rock = 15 # Jim can skip a rock 15 times
    jim_total_skips = jim_skips_per_rock * num_rocks_skipped

    # L3
    total_skips = bob_total_skips + jim_total_skips

    # FA
    answer = total_skips
    return answer