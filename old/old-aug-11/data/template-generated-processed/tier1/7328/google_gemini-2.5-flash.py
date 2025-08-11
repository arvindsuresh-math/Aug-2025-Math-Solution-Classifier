def solve():
    """Index: 7328.
    Returns: the number of individuals left at the zoo.
    """
    # L1
    class_students = 10 # class of 10 students
    num_classes = 2 # merged with another class with the same amount of students
    total_students = class_students * num_classes

    # L2
    num_parents_chaperone = 5 # 5 parents offered to be a chaperone
    total_with_parents = total_students + num_parents_chaperone

    # L3
    num_teachers = 2 # 2 of the teachers from both classes will be there too
    total_with_teachers = total_with_parents + num_teachers

    # L4
    students_left = 10 # 10 of them left
    after_students_left = total_with_teachers - students_left

    # L5
    chaperones_left = 2 # Two of the chaperones were parents in that group, so they left as well
    individuals_left_at_zoo = after_students_left - chaperones_left

    # FA
    answer = individuals_left_at_zoo
    return answer