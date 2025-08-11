def solve():
    """Index: 4869.
    Returns: the total number of blisters Brenda has.
    """
    # L1
    blisters_per_arm = 60 # 60 blisters on each arm
    num_arms = 2 # WK
    blisters_on_arms = blisters_per_arm * num_arms

    # L2
    blisters_on_rest_of_body = 80 # 80 blisters on the rest of her body
    total_blisters = blisters_on_arms + blisters_on_rest_of_body

    # FA
    answer = total_blisters
    return answer