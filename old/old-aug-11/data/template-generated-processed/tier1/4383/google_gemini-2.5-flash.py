def solve():
    """Index: 4383.
    Returns: the total drops of glue needed for the newspaper clippings.
    """
    # L1
    clippings_per_friend = 3 # three clippings for each friend
    num_friends = 7 # seven closest friends
    total_clippings = clippings_per_friend * num_friends

    # L2
    drops_per_clipping = 6 # six drops of glue to stick down each clipping
    total_glue_drops = drops_per_clipping * total_clippings

    # FA
    answer = total_glue_drops
    return answer