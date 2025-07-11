def solve():
    """Index: 137.
    Returns: the number of loads of laundry needed to wash all the oversized beach towels.
    """
    # L1
    num_families = 3 # 3 families
    people_per_family = 4 # 4 people
    total_people = num_families * people_per_family

    # L2
    towels_per_person_per_day = 1 # Everyone uses 1 oversized beach towel a day
    towels_per_day = towels_per_person_per_day * total_people

    # L3
    num_days = 7 # for 7 days
    total_towels = towels_per_day * num_days

    # L4
    machine_capacity = 14 # washing machine can hold 14 oversized beach towels per load
    loads_of_laundry = total_towels / machine_capacity

    # FA
    answer = loads_of_laundry
    return answer