def solve():
    """Index: 1385.
    Returns: the total amount Cole has to pay for the fence.
    """
    # L1
    fencing_cost_per_foot = 3 # Fencing costs $3 per foot
    side_length = 9 # 9 feet along the sides
    cost_one_side_fence = fencing_cost_per_foot * side_length

    # L2
    left_neighbor_numerator = 2 # a third of their shared side
    left_neighbor_denominator = 3 # a third of their shared side
    cost_shared_left_fence = cost_one_side_fence * left_neighbor_numerator / left_neighbor_denominator

    # L3
    back_length = 18 # 18 feet along the back
    cost_full_back_fence = fencing_cost_per_foot * back_length

    # L4
    back_fence_share_denominator = 2 # half of their shared side
    cost_cole_back_fence = cost_full_back_fence / back_fence_share_denominator

    # L5
    total_cost_cole = cost_shared_left_fence + cost_one_side_fence + cost_cole_back_fence

    # FA
    answer = total_cost_cole
    return answer