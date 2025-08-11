def solve():
    """Index: 5732.
    Returns: the average marks for the whole class.
    """
    # L1
    marks_group1 = 90 # 90 marks
    num_students_group1 = 10 # ten students
    total_marks_group1 = marks_group1 * num_students_group1

    # L2
    marks_fewer = 10 # ten marks fewer
    marks_group2_each = marks_group1 - marks_fewer

    # L3
    num_students_group2 = 15 # 15 scored
    total_marks_group2 = num_students_group2 * marks_group2_each

    # L4
    num_students_above_sixty = num_students_group1 + num_students_group2

    # L5
    total_students_class = 50 # The number of students in Kylie's class is 50
    num_students_group3 = total_students_class - num_students_above_sixty

    # L6
    marks_group3 = 60 # the rest scored 60 marks each
    total_marks_group3 = marks_group3 * num_students_group3

    # L7
    total_marks_class = total_marks_group3 + total_marks_group2 + total_marks_group1

    # L8
    average_marks = total_marks_class / total_students_class

    # FA
    answer = average_marks
    return answer