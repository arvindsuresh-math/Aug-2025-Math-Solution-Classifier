def solve():
    """Index: 5148.
    Returns: the total number of students Monica sees each day.
    """
    # L1
    first_class_students = 20 # The first class has 20 students
    second_class_students = 25 # The second and third classes have 25 students
    third_class_students = 25 # The second and third classes have 25 students
    fifth_class_students = 28 # Her fifth and sixth classes have 28 students
    sixth_class_students = 28 # Her fifth and sixth classes have 28 students
    students_in_five_classes = first_class_students + second_class_students + third_class_students + fifth_class_students + sixth_class_students

    # L2
    half_divisor = 2 # half as many as her first class
    fourth_class_students = first_class_students / half_divisor

    # L3
    total_students_per_day = students_in_five_classes + fourth_class_students

    # FA
    answer = total_students_per_day
    return answer