def solve():
    """Index: 408.
    Returns: the maximum weight of the next person who can enter the elevator without exceeding the limit.
    """
    # L1
    avg_adult_weight = 140 # average weight is 140 pounds
    num_adults = 3 # three adults
    total_adult_weight = avg_adult_weight * num_adults

    # L2
    avg_child_weight = 64 # average weight is 64 pounds
    num_children = 2 # two children
    total_child_weight = avg_child_weight * num_children

    # L3
    total_weight = total_adult_weight + total_child_weight

    # L4
    max_elevator_weight = 600 # Maximum weight 600 pounds
    max_next_person_weight = max_elevator_weight - total_weight

    # FA
    answer = max_next_person_weight
    return answer