def solve():
    """Index: 647.
    Returns: the number of cupcakes Quinton had left over after giving them out.
    """
    # L1
    initial_cupcakes = 40 # Quinton brought 40 cupcakes to school
    ms_delmont_students = 18 # 18 students in Ms. Delmont's class
    after_delmont = initial_cupcakes - ms_delmont_students

    # L2
    mrs_donnelly_students = 16 # 16 students in Mrs. Donnelly's class
    after_donnelly = after_delmont - mrs_donnelly_students

    # L3
    ms_delmont = 1 # gave a cupcake to Ms. Delmont
    mrs_donnelly = 1 # gave a cupcake to Mrs. Donnelly
    nurse = 1 # gave a cupcake to the school nurse
    principal = 1 # gave a cupcake to the school principal
    cupcakes_left = after_donnelly - ms_delmont - mrs_donnelly - nurse - principal

    # FA
    answer = cupcakes_left
    return answer