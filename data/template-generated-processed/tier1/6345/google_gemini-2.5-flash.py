def solve():
    """Index: 6345.
    Returns: the total number of leaves on all the ferns.
    """
    # L1
    fronds_per_fern = 7 # 7 fronds
    num_ferns = 6 # 6 ferns
    total_fronds = fronds_per_fern * num_ferns

    # L2
    leaves_per_frond = 30 # 30 leaves
    total_leaves = total_fronds * leaves_per_frond

    # FA
    answer = total_leaves
    return answer