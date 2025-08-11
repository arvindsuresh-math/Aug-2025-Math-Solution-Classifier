def solve():
    """Index: 6442.
    Returns: the number of hot dog buns each student can get.
    """
    # L1
    packages_bought = 30 # 30 packages of hot dog buns
    buns_per_package = 8 # packages of 8
    total_buns = packages_bought * buns_per_package

    # L2
    num_classes = 4 # four classes
    students_per_class = 30 # 30 students in each class
    total_students = num_classes * students_per_class

    # L3
    buns_per_student = total_buns / total_students

    # FA
    answer = buns_per_student
    return answer