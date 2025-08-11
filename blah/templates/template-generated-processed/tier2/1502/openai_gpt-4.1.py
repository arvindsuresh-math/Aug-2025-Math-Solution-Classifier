def solve():
    """Index: 1502.
    Returns: the number of cupcakes left after Dani gives one to everyone in the class.
    """
    # L1
    dozens_brought = 2.5 # two and half dozen cupcakes
    dozen = 12 # WK
    total_cupcakes = dozens_brought * dozen

    # L2
    num_students = 27 # 27 students (including Dani)
    num_teachers = 1 # 1 teacher
    num_aids = 1 # 1 teacher’s aid
    total_people = num_students + num_teachers + num_aids

    # L3
    num_sick = 3 # 3 students called in sick
    people_present = total_people - num_sick

    # L4
    cupcakes_left = total_cupcakes - people_present

    # FA
    answer = cupcakes_left
    return answer