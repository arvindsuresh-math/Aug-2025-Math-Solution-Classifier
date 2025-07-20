def solve():
    """Index: 6977.
    Returns: the number of boys absent that day.
    """
    # L1
    girls_present = 140 # all the 140 girls were present
    girls_per_boy_ratio = 2 # twice as many girls as boys present
    boys_present = girls_present / girls_per_boy_ratio

    # L2
    students_present = girls_present + boys_present

    # L3
    total_class_students = 250 # The class has 250 students
    boys_absent = total_class_students - students_present

    # FA
    answer = boys_absent
    return answer