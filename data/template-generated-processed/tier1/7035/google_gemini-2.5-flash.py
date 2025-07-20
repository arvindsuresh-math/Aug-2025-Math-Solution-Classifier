def solve():
    """Index: 7035.
    Returns: the minimum grade Ahmed needs to get to beat Emily.
    """
    # L1
    num_assignments = 9 # 9 assignments
    ahmed_current_grade = 91 # Ahmed has a 91 in the class
    ahmed_current_total_points = num_assignments * ahmed_current_grade

    # L2
    emily_current_grade = 92 # Emily has a 92
    emily_current_total_points = num_assignments * emily_current_grade

    # L3
    emily_final_assignment_grade = 90 # Emily got a 90 on the final assignment
    emily_total_points_after_final = emily_current_total_points + emily_final_assignment_grade

    # L4
    ahmed_grade_to_tie = emily_total_points_after_final - ahmed_current_total_points

    # L5
    one_point_more = 1 # WK
    ahmed_grade_to_beat = ahmed_grade_to_tie + one_point_more

    # FA
    answer = ahmed_grade_to_beat
    return answer