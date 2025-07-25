def solve():
    """Index: 7296.
    Returns: the number of classes Maddy needs to take per semester.
    """
    # L1
    total_credits_needed = 120 # 120 credits to graduate
    credits_per_class = 3 # each class is 3 credits
    total_classes_needed = total_credits_needed / credits_per_class

    # L2
    number_of_semesters = 8 # 8 semesters
    classes_per_semester = total_classes_needed / number_of_semesters

    # FA
    answer = classes_per_semester
    return answer