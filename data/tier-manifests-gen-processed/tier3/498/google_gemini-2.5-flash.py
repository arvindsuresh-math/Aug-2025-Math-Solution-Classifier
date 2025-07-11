def solve():
    """Index: 498.
    Returns: the number of additional bags the plane can hold at maximum weight.
    """
    # L1
    bags_per_person = 5 # each have 5 bags of luggage
    max_bag_weight = 50 # Each of their bags weighs the maximum weight allowed, 50 pounds
    weight_per_person = bags_per_person * max_bag_weight

    # L2
    num_people = 6 # 6 people going on an airplane trip
    current_luggage_weight = num_people * weight_per_person

    # L3
    plane_max_weight = 6000 # The airplane can hold a total luggage weight of 6000 pounds
    remaining_luggage_capacity = plane_max_weight - current_luggage_weight

    # L4
    additional_bags_possible = remaining_luggage_capacity / max_bag_weight

    # FA
    answer = additional_bags_possible
    return answer