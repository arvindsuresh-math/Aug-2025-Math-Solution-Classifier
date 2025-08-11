def solve():
    """Index: 1448.
    Returns: the total number of notebooks in the classroom.
    """
    # L1
    total_students = 28 # There are 28 students in a classroom
    half_divisor = 2 # Half of them
    half_class_students = total_students / half_divisor

    # L2
    notebooks_per_student_group1 = 3 # the other half have 3 notebooks each
    notebooks_group1 = half_class_students * notebooks_per_student_group1

    # L3
    notebooks_per_student_group2 = 5 # Half of them have 5 notebooks each
    notebooks_group2 = half_class_students * notebooks_per_student_group2

    # L4
    total_notebooks = notebooks_group1 + notebooks_group2

    # FA
    answer = total_notebooks
    return answer