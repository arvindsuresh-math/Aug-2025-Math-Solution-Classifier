def solve():
    """Index: 498.
    Returns: the number of additional bags at maximum weight the plane can hold.
    """
    # L1
    bags_per_person = 5 # each have 5 bags of luggage
    max_weight_per_bag = 50 # each bag weighs the maximum weight allowed, 50 pounds
    weight_per_person = bags_per_person * max_weight_per_bag

    # L2
    num_people = 6 # There are 6 people
    total_luggage_weight = num_people * weight_per_person

    # L3
    plane_capacity = 6000 # The airplane can hold a total luggage weight of 6000 pounds
    remaining_capacity = plane_capacity - total_luggage_weight

    # L4
    additional_bags = remaining_capacity / max_weight_per_bag

    # FA
    answer = additional_bags
    return answer