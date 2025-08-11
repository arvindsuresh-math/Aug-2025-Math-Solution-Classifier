def solve():
    """Index: 3454.
    Returns: the number of students still enrolled.
    """
    # L1
    initial_students = 8 # currently has 8 students enrolled
    new_interested_students = 8 # 8 more became interested
    students_after_initial_interest = initial_students + new_interested_students

    # L2
    dropout_fraction_new_recruits = 0.25 # a fourth of these dropped out
    new_recruits_dropped_out = new_interested_students * dropout_fraction_new_recruits

    # L3
    frustrated_students_left = 2 # 2 more got frustrated and left
    students_after_initial_dropouts = students_after_initial_interest - new_recruits_dropped_out - frustrated_students_left

    # L4
    enrollment_increase_factor = 5 # increased enrollment by 5 times the amount of students already enrolled
    students_after_rally_increase = students_after_initial_dropouts * enrollment_increase_factor + students_after_initial_dropouts

    # L5
    scheduling_conflict_dropouts = 2 # 2 had to drop it because of scheduling conflicts
    students_after_scheduling_dropouts = students_after_rally_increase - scheduling_conflict_dropouts

    # L6
    final_rally_enrollment = 6 # 6 more people enrolled
    students_after_final_rally = students_after_scheduling_dropouts + final_rally_enrollment

    # L7
    class_drop_divisor = 2 # half of the class eventually dropped
    students_after_class_drop = students_after_final_rally / class_drop_divisor

    # L8
    graduated_divisor = 2 # half of the remaining students graduated
    students_remaining = students_after_class_drop / graduated_divisor

    # FA
    answer = students_remaining
    return answer