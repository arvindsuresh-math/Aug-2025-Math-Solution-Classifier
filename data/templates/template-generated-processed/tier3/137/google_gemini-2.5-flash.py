def solve():
    """Index: 137.
    Returns: the total number of loads of laundry required.
    """
    # L1
    num_families = 3 # 3 families
    people_per_family = 4 # 4 people
    total_people = num_families * people_per_family

    # L2
    towels_per_person_per_day = 1 # 1 oversized beach towel a day
    towels_per_day = towels_per_person_per_day * total_people

    # L3
    vacation_days = 7 # for 7 days
    total_towels_used = towels_per_day * vacation_days

    # L4
    washer_capacity = 14 # can hold 14 oversized beach towels per load
    num_loads = total_towels_used / washer_capacity

    # FA
    answer = num_loads
    return answer