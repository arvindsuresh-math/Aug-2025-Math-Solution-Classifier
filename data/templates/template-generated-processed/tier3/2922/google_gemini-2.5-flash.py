def solve():
    """Index: 2922.
    Returns: the total number of leaves Sabrina needs.
    """
    # L1
    basil_leaves = 12 # 12 basil leaves
    basil_to_sage_ratio = 2 # twice as many basil leaves as sage leaves
    sage_leaves = basil_leaves / basil_to_sage_ratio

    # L2
    fewer_sage_than_verbena = 5 # 5 fewer sage leaves than verbena leaves
    verbena_leaves = sage_leaves + fewer_sage_than_verbena

    # L3
    total_leaves = sage_leaves + verbena_leaves + basil_leaves

    # FA
    answer = total_leaves
    return answer