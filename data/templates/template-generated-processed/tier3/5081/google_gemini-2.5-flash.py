from fractions import Fraction

def solve():
    """Index: 5081.
    Returns: the total weight the canoe was carrying.
    """
    # L1
    total_capacity = 6 # 6 people
    capacity_fraction_with_dog = Fraction(2, 3) # 2/3 of that number
    people_with_dog = capacity_fraction_with_dog * total_capacity

    # L2
    person_weight = 140 # weighed 140 pounds
    total_people_weight = person_weight * people_with_dog

    # L3
    dog_weight_fraction = Fraction(1, 4) # 1/4 as much weight
    dog_weight_divisor = 4 # 1/4 as much weight
    dog_weight = dog_weight_fraction * person_weight

    # L4
    total_canoe_weight = total_people_weight + dog_weight

    # FA
    answer = total_canoe_weight
    return answer