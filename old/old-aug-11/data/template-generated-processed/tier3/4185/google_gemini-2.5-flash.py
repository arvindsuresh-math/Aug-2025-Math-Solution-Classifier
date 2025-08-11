def solve():
    """Index: 4185.
    Returns: the number of packs Emily opened for her classmates.
    """
    # L1
    num_packs = 9 # 9 packs of candy necklaces
    necklaces_per_pack = 8 # Each pack had 8 candy necklaces in it
    total_necklaces = num_packs * necklaces_per_pack

    # L2
    necklaces_left = 40 # there were 40 candy necklaces left
    necklaces_taken = total_necklaces - necklaces_left

    # L3
    packs_opened = necklaces_taken / necklaces_per_pack

    # FA
    answer = packs_opened
    return answer