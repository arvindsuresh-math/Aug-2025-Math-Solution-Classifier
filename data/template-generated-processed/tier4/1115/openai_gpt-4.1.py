def solve():
    """Index: 1115.
    Returns: the total cost of scallops for 8 people.
    """
    # L1
    num_people = 8 # cooking for 8 people
    scallops_per_person = 2 # 2 scallops per person
    total_scallops = num_people * scallops_per_person

    # L2
    scallops_per_pound = 8 # 8 jumbo scallops weigh one pound
    total_pounds = total_scallops / scallops_per_pound

    # L3
    price_per_pound = 24 # $24.00 a pound
    total_cost = price_per_pound * total_pounds

    # FA
    answer = total_cost
    return answer