def solve():
    """Index: 2928.
    Returns: the total number of people in Oxford High School.
    """
    # L1
    num_teachers = 48 # 48 teachers
    num_principal = 1 # 1 principal
    num_classes = 15 # 15 classes
    students_per_class = 20 # 20 students
    total_students = num_classes * students_per_class

    # L2
    total_people = total_students + num_teachers + num_principal

    # FA
    answer = total_people
    return answer