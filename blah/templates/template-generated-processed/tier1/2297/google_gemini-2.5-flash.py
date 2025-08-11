def solve():
    """Index: 2297.
    Returns: the total number of beads needed.
    """
    # L1
    beads_per_necklace = 50 # 50 beads to make each necklace
    num_necklaces_per_member = 2 # 2 necklaces each
    beads_per_member = beads_per_necklace * num_necklaces_per_member

    # L2
    num_members = 9 # Nine members of the crafts club
    total_beads = num_members * beads_per_member

    # FA
    answer = total_beads
    return answer