from fractions import Fraction

def solve():
    """Index: 946.
    Returns: the total amount Ruby pays for dance lessons.
    """
    # L1
    pack_cost = 75 # $75 for 10 classes in one pack
    num_classes_in_pack = 10 # 10 classes in one pack
    cost_per_class_in_pack = pack_cost / num_classes_in_pack

    # L2
    additional_cost_fraction = Fraction(1, 3) # 1/3 more than the average price
    cost_per_additional_class = cost_per_class_in_pack * (1 + additional_cost_fraction)

    # L3
    total_classes_taken = 13 # 13 total classes
    num_extra_classes = total_classes_taken - num_classes_in_pack

    # L4
    cost_additional_classes = num_extra_classes * cost_per_additional_class

    # L5
    total_cost = pack_cost + cost_additional_classes

    # FA
    answer = total_cost
    return answer