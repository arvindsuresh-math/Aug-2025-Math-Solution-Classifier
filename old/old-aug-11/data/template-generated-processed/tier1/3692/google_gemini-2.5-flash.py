def solve():
    """Index: 3692.
    Returns: the number of students who will be unable to partner with a student of the opposite gender.
    """
    # L1
    males_class1 = 17 # 17 males
    males_class2 = 14 # 14 males
    males_class3 = 15 # 15 males
    total_male_students = males_class1 + males_class2 + males_class3

    # L2
    females_class1 = 13 # 13 females
    females_class2 = 18 # 18 females
    females_class3 = 17 # 17 females
    total_female_students = females_class1 + females_class2 + females_class3

    # L3
    unpartnered_students = total_female_students - total_male_students

    # FA
    answer = unpartnered_students
    return answer