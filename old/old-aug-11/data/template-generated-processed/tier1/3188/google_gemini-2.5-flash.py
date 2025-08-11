def solve():
    """Index: 3188.
    Returns: the total number of plates used during the visit.
    """
    # L1
    tom_count = 1 # Tom invites his parents and 3 siblings to his house.
    parents_count = 2 # Tom invites his parents
    siblings_count = 3 # 3 siblings
    total_people = tom_count + parents_count + siblings_count

    # L2
    plates_per_person_per_meal = 2 # each person uses 2 plates per meal
    plates_per_meal = total_people * plates_per_person_per_meal

    # L3
    meals_per_day = 3 # They each eat 3 times a day
    plates_per_day = plates_per_meal * meals_per_day

    # L4
    duration_days = 4 # for the 4 days
    total_plates_for_visit = plates_per_day * duration_days

    # FA
    answer = total_plates_for_visit
    return answer