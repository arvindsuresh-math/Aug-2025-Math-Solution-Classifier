def solve():
    """Index: 5581.
    Returns: the number of students who do not wear any vision assistance.
    """
    # L1
    total_students = 40 # 40 students
    glasses_percent_num = 25 # 25% of them wear glasses
    percent_factor = 0.01 # WK
    students_wear_glasses = total_students * glasses_percent_num * percent_factor

    # L2
    contact_lenses_percent_num = 40 # 40% of them wear contact lenses
    students_wear_contact_lenses = total_students * contact_lenses_percent_num * percent_factor

    # L3
    students_wear_vision_assistance = students_wear_glasses + students_wear_contact_lenses

    # L4
    students_no_vision_assistance = total_students - students_wear_vision_assistance

    # FA
    answer = students_no_vision_assistance
    return answer