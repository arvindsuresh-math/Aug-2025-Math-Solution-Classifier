def solve():
    """Index: 6415.
    Returns: the number of people who could fit on the raft.
    """
    # L1
    capacity_no_jackets = 21 # 21 people on a raft if no one wore life jackets
    fewer_with_jackets = 7 # 7 fewer people who could fit on the raft if everyone wore life jackets
    capacity_with_all_jackets = capacity_no_jackets - fewer_with_jackets

    # L2
    jackets_per_person_reduction = capacity_with_all_jackets / fewer_with_jackets

    # L3
    jackets_needed = 8 # If 8 people on the raft needed life jackets
    reduction_for_specific_jackets = jackets_needed / jackets_per_person_reduction

    # L4
    final_capacity = capacity_no_jackets - reduction_for_specific_jackets

    # FA
    answer = final_capacity
    return answer