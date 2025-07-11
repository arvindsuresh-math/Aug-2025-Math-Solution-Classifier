def solve():
    """Index: 408.
    Returns: the maximum weight of the next person to get in the elevator.
    """
    # L1
    avg_weight_adults = 140 # average weight is 140 pounds
    num_adults = 3 # Three adults
    total_weight_adults = avg_weight_adults * num_adults

    # L2
    avg_weight_children = 64 # average weight is 64 pounds
    num_children = 2 # Two children
    total_weight_children = avg_weight_children * num_children

    # L3
    current_total_weight = total_weight_adults + total_weight_children

    # L4
    max_elevator_weight = 600 # Maximum weight 600 pounds
    max_next_person_weight = max_elevator_weight - current_total_weight

    # FA
    answer = max_next_person_weight
    return answer