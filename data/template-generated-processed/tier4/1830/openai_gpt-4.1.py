def solve():
    """Index: 1830.
    Returns: the total amount Chad will spend on ice.
    """
    # L1
    num_people = 15 # total of 15 people
    pounds_per_person = 2 # 2 pounds of ice per person
    total_pounds = num_people * pounds_per_person

    # L2
    pounds_per_bag = 10 # 10-pound bags
    num_bags = total_pounds / pounds_per_bag

    # L3
    price_per_bag = 3.00 # $3.00 per bag
    total_cost = price_per_bag * num_bags

    # FA
    answer = total_cost
    return answer