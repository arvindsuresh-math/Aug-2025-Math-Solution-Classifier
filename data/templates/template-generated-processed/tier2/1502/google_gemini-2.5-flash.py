def solve():
    """Index: 1502.
    Returns: the number of cupcakes left after everyone in the class gets one.
    """
    # L1
    two_and_half_dozen = 2.5 # two and half dozen cupcakes
    cupcakes_per_dozen = 12 # WK
    total_cupcakes_brought = two_and_half_dozen * cupcakes_per_dozen

    # L2
    num_students_initial = 27 # 27 students (including Dani)
    num_teachers_and_aids = 2 # 1 teacher, and 1 teacher’s aid
    total_people_initial = num_students_initial + num_teachers_and_aids

    # L3
    students_sick = 3 # 3 students called in sick
    people_present = total_people_initial - students_sick

    # L4
    cupcakes_left = total_cupcakes_brought - people_present

    # FA
    answer = cupcakes_left
    return answer