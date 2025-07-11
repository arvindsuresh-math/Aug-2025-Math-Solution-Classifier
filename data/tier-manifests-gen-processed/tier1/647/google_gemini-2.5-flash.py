def solve():
    """Index: 647.
    Returns: the number of cupcakes Quinton had left over.
    """
    # L1
    initial_cupcakes = 40 # Quinton brought 40 cupcakes to school
    students_ms_delmont = 18 # 18 students in Ms. Delmont's class
    after_ms_delmont_class = initial_cupcakes - students_ms_delmont

    # L2
    students_mrs_donnelly = 16 # 16 students in Mrs. Donnelly's class
    after_mrs_donnelly_class = after_ms_delmont_class - students_mrs_donnelly

    # L3
    cupcake_to_adult = 1 # gave a cupcake to each of the adults (Ms. Delmont, Mrs. Donnelly, nurse, principal)
    cupcakes_left = after_mrs_donnelly_class - cupcake_to_adult - cupcake_to_adult - cupcake_to_adult - cupcake_to_adult

    # FA
    answer = cupcakes_left
    return answer