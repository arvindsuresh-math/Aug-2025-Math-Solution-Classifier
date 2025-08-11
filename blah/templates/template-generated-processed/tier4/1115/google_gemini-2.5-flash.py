def solve():
    """Index: 1115.
    Returns: the total cost of the scallops.
    """
    # L1
    num_people = 8 # cooking for 8 people
    scallops_per_person = 2 # 2 scallops with a corn bisque
    total_scallops_needed = num_people * scallops_per_person

    # L2
    scallops_per_pound = 8 # 8 jumbo scallops weigh one pound
    pounds_of_scallops_needed = total_scallops_needed / scallops_per_pound

    # L3
    cost_per_pound = 24.00 # cost $24.00 a pound
    total_cost_scallops = cost_per_pound * pounds_of_scallops_needed

    # FA
    answer = total_cost_scallops
    return answer