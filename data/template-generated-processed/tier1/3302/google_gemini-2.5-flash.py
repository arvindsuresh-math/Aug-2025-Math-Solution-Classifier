def solve():
    """Index: 3302.
    Returns: the total number of plugs.
    """
    # L1
    mittens_fewer_than_plugs = 20 # 20 fewer pairs
    mittens_pairs = 150 # box of mittens has 150 pairs of mittens
    initial_plugs_pairs = mittens_pairs + mittens_fewer_than_plugs

    # L2
    added_plugs_pairs = 30 # put 30 more pairs of plugs
    final_plugs_pairs = initial_plugs_pairs + added_plugs_pairs

    # L3
    items_per_pair = 2 # WK
    total_plugs = final_plugs_pairs * items_per_pair

    # FA
    answer = total_plugs
    return answer