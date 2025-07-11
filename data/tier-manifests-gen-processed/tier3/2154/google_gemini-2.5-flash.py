def solve():
    """Index: 2154.
    Returns: the number of people on the ship to start the journey.
    """
    # L1
    family_units_capacity = 300 # 300 family units
    people_per_family = 4 # four people per family
    full_capacity_people = family_units_capacity * people_per_family

    # L2
    capacity_fraction_denominator = 3 # one-third of the ship's capacity
    one_third_capacity = full_capacity_people / capacity_fraction_denominator

    # L3
    less_people = 100 # 100 people less
    people_on_ship_start = one_third_capacity - less_people

    # FA
    answer = people_on_ship_start
    return answer