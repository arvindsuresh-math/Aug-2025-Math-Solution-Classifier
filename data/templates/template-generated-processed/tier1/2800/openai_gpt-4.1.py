def solve():
    """Index: 2800.
    Returns: the total number of students in grades 2 and 3.
    """
    # L1
    boys_2nd = 20 # 20 boys in the second grade
    girls_2nd = 11 # 11 girls in the second grade
    students_2nd = boys_2nd + girls_2nd

    # L2
    multiplier_3rd = 2 # twice that number in the third grade
    students_3rd = students_2nd * multiplier_3rd

    # L3
    total_students = students_2nd + students_3rd

    # FA
    answer = total_students
    return answer