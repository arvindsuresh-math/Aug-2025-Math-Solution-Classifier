def solve():
    """Index: 2916.
    Returns: the total cost of beef tenderloin for the dinner party.
    """
    # L1
    num_people = 6 # inviting 6 people over
    meat_per_person = 0.5 # 1/2 pound of meat per person
    total_meat = num_people * meat_per_person

    # L2
    price_per_pound = 15.00 # $15.00 a pound
    total_cost = price_per_pound * total_meat

    # FA
    answer = total_cost
    return answer