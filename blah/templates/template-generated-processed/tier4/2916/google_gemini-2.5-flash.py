def solve():
    """Index: 2916.
    Returns: the total cost of the beef tenderloin.
    """
    # L1
    num_people = 6 # inviting 6 people over
    meat_per_person = 0.5 # 1/2 pound of meat per person
    total_meat_pounds = num_people * meat_per_person

    # L2
    cost_per_pound = 15.00 # $15.00 a pound
    total_cost = cost_per_pound * total_meat_pounds

    # FA
    answer = total_cost
    return answer