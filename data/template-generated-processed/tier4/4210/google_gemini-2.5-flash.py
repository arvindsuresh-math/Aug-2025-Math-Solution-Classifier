def solve():
    """Index: 4210.
    Returns: the total cost of croissants.
    """
    # L1
    num_people = 24 # 24 people on the committee
    sandwiches_per_person = 2 # 2 sandwiches per person
    total_sandwiches = num_people * sandwiches_per_person

    # L2
    croissants_per_dozen = 12 # WK
    dozens_needed = total_sandwiches / croissants_per_dozen

    # L3
    cost_per_dozen = 8.00 # $8.00
    total_cost = cost_per_dozen * dozens_needed

    # FA
    answer = total_cost
    return answer