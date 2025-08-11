def solve():
    """Index: 1830.
    Returns: the total amount Chad will spend on ice.
    """
    # L1
    num_guests = 15 # 15 people
    pounds_per_person = 2 # 2 pounds of ice per person
    total_pounds_needed = num_guests * pounds_per_person

    # L2
    pounds_per_bag = 10 # 10-pound bags
    num_bags_needed = total_pounds_needed / pounds_per_bag

    # L3
    cost_per_bag = 3.00 # $3.00 for a pack of 10 (interpreted as $3.00 per 10-pound bag)
    total_cost = num_bags_needed * cost_per_bag

    # FA
    answer = total_cost
    return answer